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
from lib.functions import *
from users.models import VacancyUser
from users.forms import VacancyUserForm


class VacancyUserView(views.FormView):
    """
    空室情報閲覧ユーザー
    """
    form_class = VacancyUserForm
    template_name = 'users/vacancy_user.html'
    success_url = reverse_lazy('users_vacancy_user_list')

    def __init__(self, **kwargs):
        self.user = None
        self.target_user = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404
        if not self.user.is_company_admin:
            raise Http404

        self.back_url = self.request.GET.get('back_url', None)

        user_id = 0
        try:
            idb64 = force_text(urlsafe_base64_decode(kwargs.get('idb64')))
            if idb64.isdecimal():
                user_id = xint(idb64)
        except ValueError:
            raise Http404

        if user_id != 0:
            self.target_user = get_object_or_404(VacancyUser, pk=user_id)
        else:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.target_user:
            url = reverse_lazy('users_vacancy_user', kwargs={'idb64': self.target_user.idb64})

        if self.back_url:
            url += '?back_url=' + escape_uri_path(self.back_url)

        return url

    def get_form(self, form_class=None):
        form = super().get_form()
        form.instance = self.target_user
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial['username'] = self.target_user.username
        initial['password'] = self.target_user.password
        initial['display_name'] = self.target_user.display_name
        initial['email'] = self.target_user.email
        initial['is_active'] = self.target_user.is_active
        initial['is_company'] = self.target_user.is_company
        initial['level'] = self.target_user.level
        initial['allow_org_image'] = self.target_user.allow_org_image
        initial['trader_name'] = self.target_user.trader_name
        initial['trader_department_name'] = self.target_user.trader_department_name
        initial['trader_department_tel'] = self.target_user.trader_department_tel
        initial['trader_department_address'] = self.target_user.trader_department_address
        initial['note'] = self.target_user.note
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        context['target_user'] = self.target_user
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため保存できません。')
            return redirect(self.get_success_url())
        else:
            form.save()
            messages.success(self.request, '保存しました。')
            return super().form_valid(form)
