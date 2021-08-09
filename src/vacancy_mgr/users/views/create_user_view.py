"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from abc import ABCMeta, abstractmethod
from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, escape_uri_path
from django.utils.translation import gettext_lazy as _
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import views, login as auth_login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from dateutil.relativedelta import relativedelta
from PIL import Image
from lib.convert import *
from company.models import Staff
from users.forms import CreateUserForm


class CreateUserView(views.FormView):
    """
    ユーザー作成
    """
    form_class = CreateUserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('users_user_list')

    def __init__(self, **kwargs):
        self.user = None
        self.target_user = None
        self.staff = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404
        if not self.user.is_company_admin:
            raise Http404

        self.back_url = self.request.GET.get('back_url', None)

        staff_idb64 = kwargs.get('staff_idb64')
        if staff_idb64:
            staff_id = 0
            try:
                idb64 = force_text(urlsafe_base64_decode(staff_idb64))
                if idb64.isdecimal():
                    staff_id = xint(idb64)
            except ValueError:
                staff_id = 0

            if staff_id != 0:
                self.staff = Staff.objects.get(pk=staff_id)

        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.target_user:
            url = reverse_lazy('users_user', kwargs={'idb64': self.target_user.idb64})
            back_url = xstr(reverse_lazy('users_user_list'))
            url += '?back_url=' + back_url

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['staff'] = self.staff
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため追加できません。')
        else:
            target_user = form.save(commit=False)
            target_user.first_name = '未入力'
            target_user.last_name = '未入力'
            target_user.is_active = True
            target_user.is_staff = False
            target_user.is_company = True
            target_user.is_company_admin = False

            if self.staff:
                target_user.staff = self.staff

            target_user.save()

            self.target_user = target_user
            messages.success(self.request, '追加しました。')

        return super().form_valid(form)
