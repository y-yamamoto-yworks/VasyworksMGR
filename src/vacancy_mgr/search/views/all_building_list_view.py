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
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from dateutil.relativedelta import relativedelta
from PIL import Image
from lib.convert import *
from lib.functions import *
from property.models import Building
from search.forms import SearchBuildingNameForm


class AllBuildingListView(FormView):
    """
    全建物一覧
    """
    form_class = SearchBuildingNameForm
    template_name = 'search/all_building_list.html'

    def __init__(self, **kwargs):
        self.user = None
        self.building_name = None
        self.page_number = 1

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        if request.method == 'GET':
            self.building_name = request.GET.get('name', None)

        page_number = kwargs.get('page_number')
        if page_number:
            self.page_number = xint(page_number)

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['building_name'] = self.building_name
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user

        conditions = Q(is_deleted=False)
        if self.building_name:
            conditions.add(Q(building_name__contains=self.building_name), Q.AND)

        buildings = Building.objects.filter(conditions).order_by(
            'pref__priority',
            'city__priority',
            'building_kana',
            'id',
        ).all()
        if buildings:
            paginator = Paginator(buildings, settings.BUILDING_LIST_PAGE_SIZE)
            page = paginator.get_page(self.page_number)
            context['buildings'] = page
            context['page_base_url'] = reverse_lazy('search_buildings_all')

        if self.building_name:
            context['default_building_name'] = self.building_name

        return context

    def form_valid(self, form):
        if self.request.method in ('POST', 'PUT'):
            if form.data['building_name']:
                self.building_name = form.data['building_name']

        return self.render_to_response(self.get_context_data())
