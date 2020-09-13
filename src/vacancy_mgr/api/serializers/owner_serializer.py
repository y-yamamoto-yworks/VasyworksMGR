"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from owner.models import Owner


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = (
            'id',
            'owner_name',
            'owner_kana',
        )
