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
from api.api_helper import ApiHelper
from enums.models import Pref
from masters.models import City, Area
from property.models import Building
from search.forms import SearchBuildingAreaForm


class AreaBuildingListView(FormView):
    """
    建物エリア検索
    """
    form_class = SearchBuildingAreaForm
    template_name = 'search/area_building_list.html'

    def __init__(self, **kwargs):
        self.user = None
        self.is_searched = False
        self.pref = None
        self.city = None
        self.area = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['api_key'] = ApiHelper.get_key()
        context['is_searched'] = self.is_searched

        if self.city != '0' or self.area != '0':

            conditions = Q(is_deleted=False)

            if self.area and self.area != '0':
                conditions.add(Q(area=self.area), Q.AND)
            elif self.city and self.city != '0':
                conditions.add(Q(city=self.city), Q.AND)

            buildings = Building.objects.filter(conditions).order_by(
                'pref__priority',
                'city__priority',
                'building_kana',
                'id',
            ).all()
            context['buildings'] = buildings

        else:
            context['is_searched'] = False

        if settings.DEFAULT_PREF_ID:
            context['default_pref_id'] = settings.DEFAULT_PREF_ID

        return context

    def form_valid(self, form):
        if self.request.method in ('POST', 'PUT'):
            self.is_searched = True
            if form.data.get('pref'):
                self.pref = form.data['pref']
            if form.data.get('city'):
                self.city = form.data['city']
            if form.data.get('area'):
                self.area = form.data['area']

        return self.render_to_response(self.get_context_data())
