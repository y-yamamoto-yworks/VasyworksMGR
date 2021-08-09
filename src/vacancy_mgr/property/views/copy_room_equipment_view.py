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
from lib.room_copy_helper import RoomCopyHelper
from property.forms import SelectOtherRoomForm
from users.models import User
from property.models import Room, RoomPicture


class CopyRoomEquipmentView(FormView):
    """
    部屋設備コピー
    """
    form_class = SelectOtherRoomForm
    template_name = 'property/copy_room_equipment.html'
    success_url = reverse_lazy('menu_index')

    def __init__(self, **kwargs):
        self.user = None
        self.room = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        room_oid = kwargs['room_oid']
        self.room = get_object_or_404(Room, oid=room_oid)

        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.room:
            kwargs['room'] = self.room
        return kwargs

    def get_success_url(self):
        url = super().get_success_url()
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
        context['room'] = self.room
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのためコピーできません。')
        elif self.request.method == 'POST':
            if self.room:
                selected_room_id = self.request.POST['selected_room']
                source_room = Room.objects.get(pk=selected_room_id)
                RoomCopyHelper.copy_room_equipments(
                    source_room=source_room,
                    destination_room=self.room,
                    user=self.user,
                )
                messages.success(self.request, '設備をコピーしました。')
            else:
                raise ValueError

        return super().form_valid(form)
