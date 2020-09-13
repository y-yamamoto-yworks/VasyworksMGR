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
from property.models import Room
from property.models import RoomEquipment, RoomPicture, RoomMovie, RoomPanorama, RoomVacancyTheme, RoomStatusLog


class RoomView(TemplateView):
    """
    部屋表示
    """
    template_name = 'property/room.html'
    user = None
    back_url = None
    room = None
    equipments = None
    pictures = None
    movies = None
    panoramas = None
    vacancy_themes = None
    status_logs = None
    active_page = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        page = request.GET.get('page')
        if page:
            self.active_page = page
        else:
            self.active_page = 'main_page'

        oid = kwargs['oid']
        self.room = get_object_or_404(Room, oid=oid)

        if self.room:

            self.equipments = RoomEquipment.objects.filter(
                room=self.room,
                is_deleted=False,
            ).order_by('priority', 'equipment__category__priority', 'equipment__priority', 'id').all()

            self.pictures = RoomPicture.objects.filter(
                room=self.room,
                is_deleted=False,
            ).order_by('priority', 'picture_type__priority', 'id').all()

            self.movies = RoomMovie.objects.filter(
                room=self.room,
                is_deleted=False,
            ).order_by('priority', 'movie_type__priority', 'id').all()

            self.panoramas = RoomPanorama.objects.filter(
                room=self.room,
                is_deleted=False,
            ).order_by('priority', 'panorama_type__priority', 'id').all()

            self.vacancy_themes = RoomVacancyTheme.objects.filter(
                room=self.room,
                is_deleted=False,
            ).order_by('vacancy_theme__priority', 'id').all()

            # 直近50件の部屋状況ログ
            self.status_logs = RoomStatusLog.objects.filter(
                room=self.room,
            ).order_by('-created_at').all()[:50]

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        context['room'] = self.room
        context['equipments'] = self.equipments
        context['pictures'] = self.pictures
        context['movies'] = self.movies
        context['panoramas'] = self.panoramas
        context['vacancy_themes'] = self.vacancy_themes
        context['status_logs'] = self.status_logs
        context['active_page'] = self.active_page
        context['condo_fees_name'] = settings.CONDO_FEES_NAME
        return context
