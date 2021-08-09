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
from property.models import Building, Room


class DeleteBuildingView(FormView):
    """
    建物削除
    """
    model = Building
    form_class = DeleteForm
    template_name = 'property/delete_building.html'
    success_url = reverse_lazy('search_buildings_all')

    def __init__(self, **kwargs):
        self.user = None
        self.building = None
        self.is_deletable = True

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        oid = kwargs['oid']
        self.building = get_object_or_404(Building, oid=oid)

        room_count = Room.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('room_no').all().count()

        if room_count > 0:
            self.is_deletable = False

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['data'] = self.building
        context['is_deletable'] = self.is_deletable
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため削除できません。')
        elif not self.is_deletable:
            messages.error(self.request, '部屋の登録が存在するため削除できません。')
        elif self.building:
            self.building.is_deleted = True
            self.building.updated_at = timezone.datetime.now()
            self.building.updated_user = self.user
            self.building.save()
            messages.success(self.request, '削除しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '削除に失敗しました。')
        return super().form_invalid(form)
