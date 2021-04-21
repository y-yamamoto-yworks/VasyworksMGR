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
from property.forms import UploadRoomPictureForm
from property.models import Room, RoomPicture
from enums.models import PictureType


class UploadRoomPictureView(FormView):
    """
    部屋画像アップロード
    """
    form_class = UploadRoomPictureForm
    template_name = 'property/upload_room_picture.html'
    success_url = reverse_lazy('menu_index')
    user = None
    back_url = None
    room = None
    room_picture = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        room_oid = kwargs['room_oid']
        self.room = get_object_or_404(Room, oid=room_oid)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.room_picture:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('property_room', kwargs={'oid': self.room.oid})
        elif settings.DEMO:
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
                picture_type_id = self.request.POST['picture_type']
                picture_type = PictureType.objects.get(pk=picture_type_id)

                file_name = None
                if self.request.FILES['image']:
                    image = Image.open(self.request.FILES['image'])
                    file_name = MediaHelper.get_uuid_filename(self.request.FILES['image'].name)

                    file_path = MediaHelper.get_upload_picture_path(self.room.building, file_name)
                    ImageHelper.save_image(image, file_path, settings.ORIGINAL_IMAGE_SIZE)

                    thumbnail_path = MediaHelper.get_picture_thumbnail_path(file_path)
                    ImageHelper.save_image(image, thumbnail_path, settings.THUMBNAIL_IMAGE_SIZE)

                if picture_type and file_name:
                    data = RoomPicture()
                    data.picture_type = picture_type
                    data.file_name = file_name
                    data.cache_name_thumb = MediaHelper.get_uuid_filename(file_name)
                    data.cache_name_s = MediaHelper.get_uuid_filename(file_name)
                    data.cache_name_m = MediaHelper.get_uuid_filename(file_name)
                    data.cache_name_l = MediaHelper.get_uuid_filename(file_name)
                    data.cache_name_org = MediaHelper.get_uuid_filename(file_name)
                    data.building = self.room.building
                    data.room = self.room
                    data.is_publish_web = False
                    data.is_publish_vacancy = True

                    data.created_at = timezone.datetime.now()
                    data.created_user = self.user
                    data.updated_at = timezone.datetime.now()
                    data.updated_user = self.user

                    data.save()
                    self.room_picture = data
                    messages.success(self.request, '追加しました。')
                else:
                    raise ValueError

        return super().form_valid(form)
