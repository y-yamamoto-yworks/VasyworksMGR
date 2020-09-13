"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import uuid
import urllib.parse
import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, escape_uri_path
from lib.convert import *
from api.api_helper import ApiHelper


class NewKeyViewSet(viewsets.ViewSet):
    def retrieve(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        return Response(uuid.uuid4().hex)
