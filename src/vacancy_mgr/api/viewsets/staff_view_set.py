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
from company.models import Staff
from api.serializers import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    """
    スタッフ
    """
    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        hint = kwargs.get('hint')

        conditions = Q(is_stopped=False, is_deleted=False)
        if hint:
            keywords = hint.replace('　', ' ').split(' ')
            for keyword in keywords:
                condition = Q(first_name__contains=keyword)
                condition.add(Q(last_name__contains=keyword), Q.OR)
                conditions.add(condition, Q.AND)
        conditions.add(Q(pk=0), Q.OR)

        self.queryset = Staff.objects.filter(conditions).order_by('priority').all()
        self.serializer_class = StaffSerializer

        return super().list(request, args, kwargs)
