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
from common.forms import CreateWithNameForm
from trader.models import Trader


class CreateTraderView(FormView):
    """
    賃貸管理業者作成
    """
    form_class = CreateWithNameForm
    template_name = 'trader/create_trader.html'
    success_url = reverse_lazy('trader_trader_list')

    def __init__(self, **kwargs):
        self.user = None
        self.trader = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.trader:
            url = reverse_lazy('trader_detail', kwargs={'idb64': self.trader.idb64})
            back_url = xstr(reverse_lazy('trader_trader_list'))
            url += '?back_url=' + back_url

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['trader'] = self.trader
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため追加できません。')
        elif self.request.method == 'POST':
            name = self.request.POST['name']
            kana = self.request.POST['kana']

            data = Trader()
            data.trader_name = name
            data.trader_kana = kana
            data.created_at = timezone.datetime.now()
            data.created_user = self.user
            data.updated_at = timezone.datetime.now()
            data.updated_user = self.user
            data.is_stopped = False
            data.is_deleted = False
            data.save()
            self.trader = data
            messages.success(self.request, '追加しました。')

        return super().form_valid(form)
