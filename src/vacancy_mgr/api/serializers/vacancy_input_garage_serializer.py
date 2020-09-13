"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from vacancy_item.models import VacancyInputGarage


class VacancyInputGarageSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyInputGarage
        fields = (
            'id',
            'input_contents',
        )
