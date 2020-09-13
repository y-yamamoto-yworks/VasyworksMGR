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
from vacancy_item.models import VacancyInputCancelNotice


class VacancyInputCancelNoticeListView(TemplateView):
    """
    空室入力解約通知リスト
    """
    template_name = 'vacancy_item/vacancy_input_list.html'
    user = None
    items = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404
        if not self.user.is_company_admin:
            raise Http404

        self.items = VacancyInputCancelNotice.objects.order_by('priority', 'id').all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['items'] = self.items
        context['item_name'] = '解約通知入力テキスト'
        context['create_item_url'] = '/vacancy_item/create_input_cancel_notice/'
        context['item_url'] = '/vacancy_item/input_cancel_notice/'
        return context
