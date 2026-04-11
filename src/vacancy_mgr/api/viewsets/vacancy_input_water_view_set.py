"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
import urllib.parse
import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str, escape_uri_path
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from lib.convert import *
from api.api_helper import ApiHelper
from vacancy_item.models import VacancyInputWater
from api.serializers import VacancyInputWaterSerializer


class VacancyInputWaterViewSet(viewsets.ModelViewSet):
    """
    空室情報入力（水道費）
    """
    @method_decorator(login_required)
    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        self.queryset = VacancyInputWater.objects.filter(is_stopped=False).order_by('priority').all()
        self.serializer_class = VacancyInputWaterSerializer

        return super().list(request, args, kwargs)
