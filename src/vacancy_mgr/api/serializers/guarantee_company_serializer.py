"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from masters.models import GuaranteeCompany


class GuaranteeCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = GuaranteeCompany
        fields = (
            'id',
            'name',
        )
