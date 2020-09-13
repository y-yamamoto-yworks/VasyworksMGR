"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from masters.models import Railway


class RailwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Railway
        fields = (
            'id',
            'idb64',
            'name',
            'short_name',
        )
