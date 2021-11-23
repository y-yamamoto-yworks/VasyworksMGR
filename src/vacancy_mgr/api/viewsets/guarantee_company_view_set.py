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
from masters.models import GuaranteeCompany
from api.serializers import GuaranteeCompanySerializer


class GuaranteeCompanyViewSet(viewsets.ModelViewSet):
    """
    保証会社
    """
    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        self.queryset = GuaranteeCompany.objects.filter(is_stopped=False).order_by('priority', 'id').all()
        self.serializer_class = GuaranteeCompanySerializer

        return super().list(request, args, kwargs)
