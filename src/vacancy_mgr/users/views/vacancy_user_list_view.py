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
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from dateutil.relativedelta import relativedelta
from PIL import Image
from lib.convert import *
from users.models import VacancyUser
from users.forms import SearchVacancyUserForm


class VacancyUserListView(views.FormView):
    """
    空室情報閲覧ユーザーリスト
    """
    form_class = SearchVacancyUserForm
    template_name = 'users/vacancy_user_list.html'
    user = None
    all_users = False
    vacancy_users = None
    filter_name = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404
        if not self.user.is_company_admin:
            raise Http404

        self.vacancy_users = VacancyUser.objects.order_by('username').all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['all_users'] = self.all_users
        if self.all_users:
            if self.filter_name:
                context['users'] = self.vacancy_users.filter(
                    display_name__icontains=self.filter_name,
                ).all()
            else:
                context['users'] = self.vacancy_users
        else:
            if self.filter_name:
                context['users'] = self.vacancy_users.filter(
                    is_active=True,
                    display_name__icontains=self.filter_name,
                ).all()
            else:
                context['users'] = self.vacancy_users.filter(
                    is_active=True,
                ).all()
        return context

    def form_valid(self, form):
        if self.request.method in ('POST', 'PUT'):
            if form.data['display_name']:
               self.filter_name = form.data['display_name']

        return self.render_to_response(self.get_context_data())
