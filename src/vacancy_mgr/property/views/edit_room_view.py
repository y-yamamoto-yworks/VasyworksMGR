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
from lib.log_helper import LogHelper
from api.api_helper import ApiHelper
from property.forms import EditRoomForm
from property.models import Room


class EditRoomView(UpdateView):
    """
    部屋編集
    """
    model = Room
    form_class = EditRoomForm
    template_name = 'property/edit_room.html'
    success_url = reverse_lazy('menu_index')
    user = None
    back_url = None
    room = None
    last_status = None
    query_pk_and_slug = True
    slug_field = 'building_id'
    slug_url_kwarg = 'building_id'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        oid = kwargs['oid']
        self.room = get_object_or_404(Room, oid=oid)
        if self.room:
            self.last_status = self.room.room_status

        self.kwargs['pk'] = self.room.pk
        self.kwargs['building_id'] = self.room.building.pk

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        context['room'] = self.room
        context['api_key'] = ApiHelper.get_key()
        context['move_buttons'] = True
        context['condo_fees_name'] = settings.CONDO_FEES_NAME
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため保存できません。')
            return redirect(self.get_success_url())
        else:
            form.save(commit=False)
            form.instance.updated_at = timezone.datetime.now()
            form.instance.updated_user = self.user
            form.instance.save()

            if form.instance.room_status != self.last_status:
                LogHelper.write_room_status_log(self.user, self.room, form.instance.room_status, self.last_status)

            messages.success(self.request, '保存しました。')
            return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '保存に失敗しました。')
        return super().form_invalid(form)

    def get_success_url(self):
        url = reverse_lazy('property_edit_room', kwargs={'oid': self.room.oid})

        if self.back_url:
            url += '?back_url=' + escape_uri_path(self.back_url)

        return url