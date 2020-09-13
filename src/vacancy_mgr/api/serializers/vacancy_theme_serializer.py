"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from vacancy_item.models import VacancyTheme


class VacancyThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyTheme
        fields = (
            'id',
            'idb64',
            'name',
            'title',
        )
