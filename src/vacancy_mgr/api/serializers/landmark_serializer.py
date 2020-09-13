"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from masters.models import Landmark
from .landmark_type_serializer import LandmarkTypeSerializer


class LandmarkSerializer(serializers.ModelSerializer):
    landmark_type = LandmarkTypeSerializer(many=False)

    class Meta:
        model = Landmark
        fields = (
            'id',
            'name',
            'kana',
            'short_name',
            'lat',
            'lng',
            'priority',
            'landmark_type',
        )
