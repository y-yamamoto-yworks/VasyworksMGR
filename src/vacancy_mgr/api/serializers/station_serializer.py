"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from masters.models import Station
from .railway_serializer import RailwaySerializer


class StationSerializer(serializers.ModelSerializer):
    railway = RailwaySerializer(many=False)

    class Meta:
        model = Station
        fields = (
            'id',
            'idb64',
            'name',
            'railway',
        )
