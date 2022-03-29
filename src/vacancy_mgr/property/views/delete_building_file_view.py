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
from common.forms import DeleteForm
from property.models import Building, BuildingFile


class DeleteBuildingFileView(FormView):
    """
    建物ファイル削除
    """
    model = BuildingFile
    form_class = DeleteForm
    template_name = 'property/delete_building_file.html'
    success_url = reverse_lazy('menu_index')
    query_pk_and_slug = True
    slug_field = 'building_id'
    slug_url_kwarg = 'building_id'

    def __init__(self, **kwargs):
        self.user = None
        self.building_file = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        building_oid = kwargs['building_oid']
        building = get_object_or_404(Building, oid=building_oid)

        id = kwargs['id']
        self.building_file = get_object_or_404(BuildingFile, pk=id, building=building)

        self.kwargs['pk'] = self.building_file.pk
        self.kwargs['building_id'] = building.pk

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        context['data'] = self.building_file
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため削除できません。')
        elif self.building_file:
            self.building_file.is_deleted = True
            self.building_file.updated_at = timezone.now()
            self.building_file.updated_user = self.user
            self.building_file.save()
            messages.success(self.request, '削除しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '削除に失敗しました。')
        return super().form_invalid(form)

    def get_success_url(self):
        url = super().get_success_url()
        if self.building_file:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('property_building', kwargs={'oid': self.building_file.building.oid})

        return url
