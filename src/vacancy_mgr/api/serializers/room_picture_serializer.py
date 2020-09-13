"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from property.models import RoomPicture
from .picture_type_serializer import PictureTypeSerializer


class RoomPictureSerializer(serializers.ModelSerializer):
    picture_type = PictureTypeSerializer(many=False)

    class Meta:
        model = RoomPicture
        fields = (
            'id',
            'file_name',
            'comment',
            'picture_type',
        )
