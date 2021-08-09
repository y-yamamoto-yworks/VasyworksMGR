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
from urllib.parse import urlencode
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
from enums.models import Pref, ManagementType
from property.forms import CreateBuildingForm
from property.models import Building


class CreateBuildingView(FormView):
    """
    建物作成
    """
    form_class = CreateBuildingForm
    template_name = 'property/create_building.html'
    success_url = reverse_lazy('menu_index')

    def __init__(self, **kwargs):
        self.user = None
        self.building = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.building:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('search_buildings_all')
            url += "?{0}".format(urlencode((('name', self.building.building_name),), encoding='utf-8'))
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        context['building'] = self.building
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため追加できません。')
        elif self.request.method == 'POST':
            building_name = self.request.POST['building_name']
            building_kana = self.request.POST['building_kana']

            data = Building()
            data.building_name = building_name
            data.building_kana = building_kana
            data.oid = uuid.uuid4().hex
            data.file_oid = uuid.uuid4().hex

            if settings.DEFAULT_PREF_ID:
                pref = Pref.objects.get(pk=settings.DEFAULT_PREF_ID)
                if pref:
                    data.pref = pref

            data.management_type = ManagementType.objects.get(pk=10)        # 自社管理

            data.created_at = timezone.datetime.now()
            data.created_user = self.user
            data.updated_at = timezone.datetime.now()
            data.updated_user = self.user

            data.save()
            self.building = data
            messages.success(self.request, '追加しました。')

        return super().form_valid(form)
