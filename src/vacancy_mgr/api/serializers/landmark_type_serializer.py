"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from enums.models import LandmarkType


class LandmarkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandmarkType
        fields = (
            'id',
            'name',
            'priority',
        )
