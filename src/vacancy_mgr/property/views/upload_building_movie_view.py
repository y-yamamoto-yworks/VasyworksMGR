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
from lib.image_helper import ImageHelper
from lib.media_helper import MediaHelper
from property.forms import UploadBuildingMovieForm
from property.models import Building, BuildingMovie
from enums.models import MovieType


class UploadBuildingMovieView(FormView):
    """
    建物動画アップロード
    """
    form_class = UploadBuildingMovieForm
    template_name = 'property/upload_building_movie.html'
    success_url = reverse_lazy('menu_index')
    user = None
    back_url = None
    building = None
    building_movie = None

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
        if self.building_movie:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('property_building', kwargs={'oid': self.building.oid})
        elif settings.DEMO:
            url = reverse_lazy('property_building', kwargs={'oid': self.building.oid})

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
                movie_type_id = self.request.POST['movie_type']
                movie_type = MovieType.objects.get(pk=movie_type_id)

                file_name = None
                if self.request.FILES['movie']:
                    file_name = MediaHelper.get_uuid_filename(self.request.FILES['movie'].name)
                    file_path = MediaHelper.get_upload_movie_path(self.building, file_name)
                    MediaHelper.upload_binary_file(self.request.FILES['movie'], file_path)

                if movie_type and file_name:
                    data = BuildingMovie()
                    data.movie_type = movie_type
                    data.file_name = file_name
                    data.cache_name = MediaHelper.get_uuid_filename(file_name)
                    data.building = self.building

                    data.created_at = timezone.datetime.now()
                    data.created_user = self.user
                    data.updated_at = timezone.datetime.now()
                    data.updated_user = self.user

                    data.save()
                    self.building_movie = data
                    messages.success(self.request, '追加しました。')
                else:
                    raise ValueError

        return super().form_valid(form)
