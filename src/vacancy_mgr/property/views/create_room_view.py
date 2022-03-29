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
from enums.models import RentalType
from property.forms import CreateRoomForm
from property.models import Building, Room


class CreateRoomView(FormView):
    """
    部屋作成
    """
    form_class = CreateRoomForm
    template_name = 'property/create_room.html'
    success_url = reverse_lazy('menu_index')

    def __init__(self, **kwargs):
        self.user = None
        self.building = None
        self.room = None
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
        if self.room:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('property_room', kwargs={'oid': self.room.oid})

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
                room_no = self.request.POST['room_no']
                room_floor = self.request.POST['room_floor']

                data = Room()
                data.room_no = room_no
                if room_floor:
                    data.room_floor = room_floor
                data.building = self.building
                data.oid = uuid.uuid4().hex
                data.rental_type = RentalType.objects.get(pk=10)    # 普通借家

                data.created_at = timezone.now()
                data.created_user = self.user
                data.updated_at = timezone.now()
                data.updated_user = self.user

                data.save()
                self.room = data
                messages.success(self.request, '追加しました。')
            else:
                raise ValueError

        return super().form_valid(form)
