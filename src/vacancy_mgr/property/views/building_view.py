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
from property.models import Building
from property.models import Room
from property.models import BuildingLandmark, BuildingFacility
from property.models import BuildingGarage
from property.models import BuildingPicture, BuildingMovie, BuildingPanorama, BuildingFile


class BuildingView(TemplateView):
    """
    建物表示
    """
    template_name = 'property/building.html'

    def __init__(self, **kwargs):
        self.user = None
        self.building = None
        self.rooms = None
        self.landmarks = None
        self.facilities = None
        self.garages = None
        self.pictures = None
        self.movies = None
        self.panoramas = None
        self.files = None
        self.active_page = None
        self.back_url = None

        super().__init__(**kwargs)

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
        self.building = get_object_or_404(Building, oid=oid)

        if self.building:
            self.rooms = Room.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('room_no').all()

            self.landmarks = BuildingLandmark.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('landmark__landmark_type__priority', 'priority', 'landmark__priority', 'landmark__kana').all()

            self.facilities = BuildingFacility.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('facility__priority', 'priority').all()

            self.garages = BuildingGarage.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('priority', 'id').all()

            self.pictures = BuildingPicture.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('priority', 'picture_type__priority', 'id').all()

            self.movies = BuildingMovie.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('priority', 'movie_type__priority', 'id').all()

            self.panoramas = BuildingPanorama.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('priority', 'panorama_type__priority', 'id').all()

            self.files = BuildingFile.objects.filter(
                building=self.building,
                is_deleted=False,
            ).order_by('priority', 'file_title').all()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        context['building'] = self.building
        context['rooms'] = self.rooms
        context['landmarks'] = self.landmarks
        context['facilities'] = self.facilities
        context['garages'] = self.garages
        context['pictures'] = self.pictures
        context['movies'] = self.movies
        context['panoramas'] = self.panoramas
        context['files'] = self.files
        context['active_page'] = self.active_page
        context['condo_fees_name'] = settings.CONDO_FEES_NAME
        return context
