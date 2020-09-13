"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from vacancy_item.models import VacancyInputCancelNotice


class VacancyInputCancelNoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyInputCancelNotice
        fields = (
            'id',
            'input_contents',
        )
