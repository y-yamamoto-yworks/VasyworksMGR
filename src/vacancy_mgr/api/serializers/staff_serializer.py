"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from company.models import Staff
from .department_serializer import DepartmentSerializer


class StaffSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False)

    class Meta:
        model = Staff
        fields = (
            'id',
            'idb64',
            'last_name',
            'first_name',
            'full_name',
            'staff_name',
            'department',
        )
