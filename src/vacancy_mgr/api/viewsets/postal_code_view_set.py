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
from enums.models import PostalCode
from api.serializers import PostalCodeSerializer


class PostalCodeViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        postal_code = kwargs['postal_code']
        self.queryset = PostalCode.objects.filter(postal_code=postal_code).all()
        self.serializer_class = PostalCodeSerializer
        self.lookup_field = 'postal_code'

        return super().retrieve(request, args, kwargs)
