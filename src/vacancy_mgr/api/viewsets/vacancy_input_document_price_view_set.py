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
from vacancy_item.models import VacancyInputDocumentPrice
from api.serializers import VacancyInputDocumentPriceSerializer


class VacancyInputDocumentPriceViewSet(viewsets.ModelViewSet):
    """
    空室情報入力（書類代）
    """
    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        self.queryset = VacancyInputDocumentPrice.objects.filter(is_stopped=False).order_by('priority').all()
        self.serializer_class = VacancyInputDocumentPriceSerializer

        return super().list(request, args, kwargs)
