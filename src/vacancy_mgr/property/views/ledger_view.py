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
from company.models import Company
from property.models import Room
from property.models import RoomEquipment, RoomPicture, RoomMovie, RoomPanorama, RoomVacancyTheme, RoomStatusLog
from property.models import BuildingPicture


class LedgerView(TemplateView):
    """
    物件台帳表示
    """
    template_name = 'property/ledger.html'

    def __init__(self, **kwargs):
        self.user = None
        self.company = None
        self.room = None
        self.equipments = None
        self.building_image = None
        self.layout_image = None
        self.room_image = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.company = get_object_or_404(Company, pk=settings.COMPANY_ID)

        oid = kwargs['oid']
        self.room = get_object_or_404(Room, oid=oid)

        if self.room:
            equipments = RoomEquipment.objects.filter(
                room=self.room,
                is_deleted=False,
            ).order_by('priority', 'equipment__category__priority', 'equipment__priority', 'id').all()

            for item in equipments:
                if not self.equipments:
                    self.equipments = ''
                else:
                    self.equipments += '・'
                self.equipments += item.equipment.name

            building_pictures = BuildingPicture.objects.filter(
                building=self.room.building,
                is_deleted=False,
            ).order_by('priority', 'picture_type__priority', 'id').all()

            for item in building_pictures:
                if item.picture_type.is_building_exterior:
                    self.building_image = item
                    break

            room_pictures = RoomPicture.objects.filter(
                room=self.room,
                is_deleted=False,
            ).order_by('priority', 'picture_type__priority', 'id').all()

            for item in room_pictures:
                if item.picture_type.is_layout:
                    self.layout_image = item
                    break

            for item in room_pictures:
                if item.picture_type.is_room and not item.picture_type.is_layout:
                    self.room_image = item
                    break

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['company'] = self.company
        context['room'] = self.room
        context['equipments'] = self.equipments
        context['building_image'] = self.building_image
        context['layout_image'] = self.layout_image
        context['room_image'] = self.room_image
        context['condo_fees_name'] = settings.CONDO_FEES_NAME
        return context
