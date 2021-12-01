"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from enums.models import CondoFeesType
import warnings


class CondoFeesTypeModelTest(TestCase):
    """
    共益費種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_is_money(self):
        self.assertFalse(CondoFeesType.objects.get(pk=0).is_money)
        self.assertTrue(CondoFeesType.objects.get(pk=10).is_money)
        self.assertFalse(CondoFeesType.objects.get(pk=20).is_money)
        self.assertFalse(CondoFeesType.objects.get(pk=21).is_money)
        self.assertFalse(CondoFeesType.objects.get(pk=30).is_money)
