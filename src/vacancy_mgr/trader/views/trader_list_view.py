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
from trader.models import Trader
from trader.forms import SearchTraderNameForm


class TraderListView(FormView):
    """
    賃貸管理業者リスト
    """
    form_class = SearchTraderNameForm
    template_name = 'trader/trader_list.html'
    all_traders = False

    def __init__(self, **kwargs):
        self.user = None
        self.trader_name = None
        self.traders = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        if request.method == 'GET':
            self.trader_name = request.GET.get('name', None)

        self.traders = Trader.objects.order_by('trader_kana', 'id').all()
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['trader_name'] = self.trader_name
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['all_traders'] = self.all_traders

        if self.all_traders and self.trader_name is None:
            context['traders'] = self.traders
        elif self.all_traders:
            context['traders'] = self.traders.filter(trader_name__contains=self.trader_name).all()
            context['default_trader_name'] = self.trader_name
        elif self.trader_name is None:
            context['traders'] = self.traders.filter(is_deleted=False).all()
        else:
            context['traders'] = self.traders.filter(is_deleted=False, trader_name__contains=self.trader_name).all()
            context['default_trader_name'] = self.trader_name

        return context

    def form_valid(self, form):
        if self.request.method in ('POST', 'PUT'):
            if form.data['trader_name']:
                self.trader_name = form.data['trader_name']

        return self.render_to_response(self.get_context_data())
