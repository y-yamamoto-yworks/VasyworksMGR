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
from property.forms import EditRoomPanoramaForm
from property.models import Room, RoomPanorama


class EditRoomPanoramaView(UpdateView):
    """
    部屋パノラマ編集
    """
    model = RoomPanorama
    form_class = EditRoomPanoramaForm
    template_name = 'property/edit_room_panorama.html'
    success_url = reverse_lazy('menu_index')
    query_pk_and_slug = True
    slug_field = 'room_id'
    slug_url_kwarg = 'room_id'

    def __init__(self, **kwargs):
        self.user = None
        self.room_panorama = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        room_oid = kwargs['room_oid']
        room = get_object_or_404(Room, oid=room_oid)

        id = kwargs['id']
        self.room_panorama = get_object_or_404(RoomPanorama, pk=id, room=room)

        self.kwargs['pk'] = self.room_panorama.pk
        self.kwargs['room_id'] = room.pk

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        context['data'] = self.room_panorama
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため保存できません。')
            return redirect(self.get_success_url())
        else:
            form.save(commit=False)
            form.instance.updated_at = timezone.now()
            form.instance.updated_user = self.user
            form.instance.save()
            messages.success(self.request, '保存しました。')
            return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '保存に失敗しました。')
        return super().form_invalid(form)

    def get_success_url(self):
        url = super().get_success_url()
        if self.room_panorama:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('property_room', kwargs={'oid': self.room_panorama.room.oid})

        return url
