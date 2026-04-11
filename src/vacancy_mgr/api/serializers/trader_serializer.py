"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from trader.models import Trader


class TraderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trader
        fields = (
            'id',
            'trader_name',
            'trader_kana',
        )
