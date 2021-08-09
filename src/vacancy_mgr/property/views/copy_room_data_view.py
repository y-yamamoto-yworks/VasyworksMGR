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
from property.forms import CopyRoomDataForm
from users.models import User
from property.models import Room


class CopyRoomDataView(FormView):
    """
    部屋データコピー
    """
    form_class = CopyRoomDataForm
    template_name = 'property/copy_room_data.html'
    success_url = reverse_lazy('menu_index')

    def __init__(self, **kwargs):
        self.user = None
        self.room = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        oid = kwargs['oid']
        self.room = get_object_or_404(Room, oid=oid)

        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.room:
            kwargs['room'] = self.room
        return kwargs


    def get_success_url(self):
        url = super().get_success_url()
        if self.room:
            url = reverse_lazy('property_edit_room', kwargs={'oid': self.room.oid})

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['room'] = self.room
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのためコピーできません。')
        elif self.request.method == 'POST':
            if self.room:
                selected_room_id = self.request.POST['selected_room']
                source_room = Room.objects.get(pk=selected_room_id)

                base = bool(self.request.POST.get('base'))
                vacancy = bool(self.request.POST.get('vacancy'))
                web = bool(self.request.POST.get('web'))
                layout = bool(self.request.POST.get('layout'))
                monthly_cost = bool(self.request.POST.get('monthly_cost'))
                initial_cost = bool(self.request.POST.get('initial_cost'))
                renewal_cost = bool(self.request.POST.get('renewal_cost'))
                features = bool(self.request.POST.get('features'))

                if source_room:
                    RoomCopyHelper.copy_room_data(
                        source=source_room,
                        destination_room=self.room,
                        user=self.user,
                        base=base,
                        vacancy=vacancy,
                        web=web,
                        layout=layout,
                        monthly_cost=monthly_cost,
                        initial_cost=initial_cost,
                        renewal_cost=renewal_cost,
                        features=features,
                    )
                    messages.success(self.request, '{0} 号室のデータをコピーしました。'.format(source_room.room_no))
            else:
                raise ValueError

        return super().form_valid(form)
