"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import urllib.parse
import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, escape_uri_path
from lib.convert import *
from api.api_helper import ApiHelper
from enums.models import LandmarkType
from api.serializers import LandmarkTypeSerializer


class LandmarkTypeViewSet(viewsets.ModelViewSet):
    """
    ランドマーク種別
    """
    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        self.queryset = LandmarkType.objects.filter(
            Q(is_stopped=False) | Q(pk=0)
        ).order_by('priority').all()
        self.serializer_class = LandmarkTypeSerializer

        return super().list(request, args, kwargs)
