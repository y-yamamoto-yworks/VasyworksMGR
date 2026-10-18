"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
import uuid
import urllib.parse
import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str, escape_uri_path
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from lib.convert import *
from api.api_helper import ApiHelper


class NewKeyViewSet(viewsets.ViewSet):
    """
    新規キー
    """
    @method_decorator(login_required)
    def retrieve(self, request, *args, **kwargs):
        if not ApiHelper.check_key(request):
            raise PermissionDenied("Permission denied")

        return Response(uuid.uuid4().hex)
