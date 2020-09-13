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
from property.forms import CreateRoomVacancyThemeForm
from property.models import Room, RoomVacancyTheme
from vacancy_item.models import VacancyTheme


class CreateRoomVacancyThemeView(FormView):
    """
    部屋空室テーマ作成
    """
    form_class = CreateRoomVacancyThemeForm
    template_name = 'property/create_room_vacancy_theme.html'
    success_url = reverse_lazy('menu_index')
    user = None
    back_url = None
    room = None
    room_vacancy_theme = None

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
        if self.user:
            kwargs['user'] = self.user
        return kwargs

    def get_success_url(self):
        url = super().get_success_url()
        if self.room_vacancy_theme:
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
                vacancy_theme_id = self.request.POST['vacancy_theme']
                vacancy_theme = VacancyTheme.objects.get(pk=vacancy_theme_id)
                room_vacancy_themes = RoomVacancyTheme.objects.filter(room=self.room).all()

                is_exists = False
                if room_vacancy_themes:
                    for item in room_vacancy_themes:
                        if item.vacancy_theme == vacancy_theme:
                            self.room_vacancy_theme = item

                            # 既に登録済みなら追加しない
                            is_exists = True
                            if item.is_deleted:
                                # 削除されている場合は復活させる
                                item.is_deleted = False
                                item.updated_at = timezone.datetime.now()
                                item.updated_user = self.user
                                item.save()
                                messages.success(self.request, '追加しました。')

                            break

                if not is_exists:
                    if vacancy_theme:
                        data = RoomVacancyTheme()
                        data.vacancy_theme = vacancy_theme
                        data.room = self.room
                        data.building = self.room.building

                        data.created_at = timezone.datetime.now()
                        data.created_user = self.user
                        data.updated_at = timezone.datetime.now()
                        data.updated_user = self.user

                        data.save()
                        self.room_vacancy_theme = data
                        messages.success(self.request, '追加しました。')
            else:
                raise ValueError

        return super().form_valid(form)
