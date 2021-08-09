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
from property.forms import CreateRoomEquipmentForm
from property.models import Room, RoomEquipment
from enums.models import Equipment, EquipmentCategory


class CreateRoomEquipmentView(FormView):
    """
    部屋設備作成
    """
    form_class = CreateRoomEquipmentForm
    template_name = 'property/create_room_equipment.html'
    success_url = reverse_lazy('menu_index')

    def __init__(self, **kwargs):
        self.user = None
        self.room = None
        self.room_equipment = None
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

    def post(self, request, *args, **kwargs):
        if 'load_equipments' in self.request.POST:
            return self.get_response_for_load()
        else:
            return super().post(request, *args, **kwargs)

    def get_response_for_load(self):
        # 設備絞り込み用のレスポンスを返す。
        form = CreateRoomEquipmentForm()
        context = self.get_context_data()
        equipment_category_id = self.request.POST['equipment_category']
        if equipment_category_id:
            equipment_category = EquipmentCategory.objects.filter(id=equipment_category_id).first()
            if equipment_category:
                form = CreateRoomEquipmentForm(category=equipment_category)

        context['form'] = form
        return TemplateResponse(self.request, 'property/create_room_equipment.html', context=context)

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
            messages.error(self.request, 'DEMOモードのため追加できません。')
        elif self.request.method == 'POST':
            if self.room:
                equipment_ids = self.request.POST.getlist('equipments')
                is_remained = self.request.POST.get('is_remained')
                room_equipments = RoomEquipment.objects.filter(room=self.room).all()

                if len(equipment_ids) > 0:
                    for equipment_id in equipment_ids:

                        equipment = Equipment.objects.get(pk=equipment_id)
                        if equipment:
                            is_exists = False
                            if room_equipments:
                                for item in room_equipments:
                                    if item.equipment == equipment:
                                        self.room_equipment = item

                                        # 既に登録済みなら追加しない
                                        is_exists = True
                                        if item.is_deleted:
                                            # 削除されている場合は復活させる
                                            item.is_deleted = False
                                            if is_remained:
                                                item.is_remained = True
                                            else:
                                                item.is_remained = False

                                            item.updated_at = timezone.datetime.now()
                                            item.updated_user = self.user
                                            item.save()
                                            messages.success(self.request, '追加しました。')

                                        break

                            if not is_exists:
                                data = RoomEquipment()
                                data.equipment = equipment
                                if is_remained:
                                    data.is_remained = True
                                data.room = self.room
                                data.building = self.room.building

                                data.created_at = timezone.datetime.now()
                                data.created_user = self.user
                                data.updated_at = timezone.datetime.now()
                                data.updated_user = self.user

                                data.save()
                                self.room_equipment = data
                                messages.success(self.request, '追加しました。')
                else:
                    messages.error(self.request, '設備が選択されていません。')
                    return self.get_response_for_load()
            else:
                raise ValueError

        return super().form_valid(form)
