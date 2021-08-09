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
from users.models import VacancyUser
from users.forms import ChangeUserPasswordForm


class ChangeVacancyUserPasswordView(views.PasswordChangeView):
    """
    空室情報閲覧ユーザーパスワード変更
    """
    form_class = ChangeUserPasswordForm
    template_name = 'users/change_vacancy_user_password.html'
    success_url = reverse_lazy('users_vacancy_user_list')

    def __init__(self, **kwargs):
        self.user = None
        self.target_user = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404
        if not self.user.is_company_admin:
            raise Http404

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
            url = '/users/vacancy_user/{idb64}'.format(idb64=self.target_user.idb64)

        return url

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance = self.target_user
        form.user = self.target_user
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['target_user'] = self.target_user
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのためパスワードを変更できません。')
            return redirect(self.get_success_url())
        else:
            form.save()
            messages.success(self.request, 'パスワードを変更しました。')
            return super().form_valid(form)

