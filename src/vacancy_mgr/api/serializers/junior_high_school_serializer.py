"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from masters.models import JuniorHighSchool
from .pref_serializer import PrefSerializer


class JuniorHighSchoolSerializer(serializers.ModelSerializer):
    pref = PrefSerializer(many=False)

    class Meta:
        model = JuniorHighSchool
        fields = (
            'id',
            'idb64',
            'name',
            'lat',
            'lng',
            'pref',
        )
