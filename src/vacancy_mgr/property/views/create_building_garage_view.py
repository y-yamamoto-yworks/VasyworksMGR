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
from property.forms import CreateBuildingGarageForm
from property.models import Building, BuildingGarage
from enums.models import GarageStatus


class CreateBuildingGarageView(FormView):
    """
    建物ガレージ作成
    """
    form_class = CreateBuildingGarageForm
    template_name = 'property/create_building_garage.html'
    success_url = reverse_lazy('menu_index')

    def __init__(self, **kwargs):
        self.user = None
        self.building = None
        self.building_garage = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        building_oid = kwargs['building_oid']
        self.building = get_object_or_404(Building, oid=building_oid)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.building_garage:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('property_building', kwargs={'oid': self.building.oid})

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
            if self.building:
                garage_name = self.request.POST['garage_name']
                garage_status_id = self.request.POST['garage_status']

                garage_status = GarageStatus.objects.get(pk=garage_status_id)

                if garage_status:
                    data = BuildingGarage()
                    data.garage_name = garage_name
                    data.garage_status = garage_status
                    data.building = self.building

                    data.created_at = timezone.now()
                    data.created_user = self.user
                    data.updated_at = timezone.now()
                    data.updated_user = self.user

                    data.save()
                    self.building_garage = data
                    messages.success(self.request, '追加しました。')
            else:
                raise ValueError

        return super().form_valid(form)
