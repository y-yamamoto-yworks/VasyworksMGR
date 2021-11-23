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
from company.models import Department
from api.serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    部署
    """
    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        hint = kwargs.get('hint')

        conditions = Q(is_stopped=False, is_deleted=False)
        conditions.add(Q(pk=0), Q.OR)

        self.queryset = Department.objects.filter(conditions).order_by('priority').all()
        self.serializer_class = DepartmentSerializer

        return super().list(request, args, kwargs)
