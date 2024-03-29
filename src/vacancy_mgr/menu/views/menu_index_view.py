"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
import uuid
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
from django.views.generic import TemplateView, FormView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from dateutil.relativedelta import relativedelta
from PIL import Image
from lib.convert import *
from company.models import Company


class MenuIndexView(TemplateView):
    """
    メニュー
    """
    template_name = 'menu/index.html'

    def __init__(self, **kwargs):
        self.user = None
        self.company = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.company = get_object_or_404(Company, pk=settings.COMPANY_ID)

        if not self.company.api_key or not self.company.internal_api_key:
            # 会社のAPIキーがない場合は生成する。
            try:
                if not self.company.api_key:
                    self.company.api_key = uuid.uuid4().hex
                
                if not self.company.internal_api_key:
                    self.company.internal_api_key = uuid.uuid4().hex
                
                self.company.save()
            except:
                raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['company'] = self.company
        return context
