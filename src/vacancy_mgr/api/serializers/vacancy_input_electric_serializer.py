"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from vacancy_item.models import VacancyInputElectric


class VacancyInputElectricSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyInputElectric
        fields = (
            'id',
            'input_contents',
        )
