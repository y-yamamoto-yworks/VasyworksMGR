"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from enums.models import PostalCode
from .pref_serializer import PrefSerializer
from .city_serializer import CitySerializer


class PostalCodeSerializer(serializers.ModelSerializer):
    pref = PrefSerializer(many=False)
    city = CitySerializer(many=False)

    class Meta:
        model = PostalCode
        fields = (
            'id',
            'postal_code',
            'pref',
            'city',
            'town_name',
        )

