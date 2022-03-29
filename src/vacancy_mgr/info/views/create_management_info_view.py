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
from django.views.generic import TemplateView, FormView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from dateutil.relativedelta import relativedelta
from PIL import Image
from lib.convert import *
from lib.functions import *
from info.forms import CreateManagementInfoForm
from info.models import ManagementInfo


class CreateManagementInfoView(FormView):
    """
    管理お知らせ作成
    """
    form_class = CreateManagementInfoForm
    template_name = 'info/create_management_info.html'
    success_url = reverse_lazy('info_management_info_list')

    def __init__(self, **kwargs):
        self.user = None
        self.info = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.info:
            url = reverse_lazy('info_edit_management_info', kwargs={'idb64': self.info.idb64})
            back_url = xstr(reverse_lazy('info_management_info_list'))
            url += '?back_url=' + back_url

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['info'] = self.info
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため追加できません。')
        elif self.request.method == 'POST':
            information = self.request.POST.get('information')
            start_date = self.request.POST.get('start_date')
            end_date = self.request.POST.get('end_date')
            link_url = self.request.POST.get('link_url')
            is_emphasized = False
            if self.request.POST.get('is_emphasized'):
                is_emphasized = True

            data = ManagementInfo()
            data.information = information
            data.start_date = start_date
            data.end_date = end_date
            data.link_url = link_url
            data.is_emphasized = is_emphasized
            data.created_at = timezone.now()
            data.created_user = self.user
            data.updated_at = timezone.now()
            data.updated_user = self.user
            data.is_stopped = False
            data.is_deleted = False
            data.save()
            self.info = data
            messages.success(self.request, '追加しました。')

        return super().form_valid(form)
