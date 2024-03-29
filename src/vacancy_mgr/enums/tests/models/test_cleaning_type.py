"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from enums.models import CleaningType
import warnings


class CleaningTypeModelTest(TestCase):
    """
    退去時清掃種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_money(self):
        self.assertFalse(CleaningType.objects.get(pk=0).is_money)
        self.assertFalse(CleaningType.objects.get(pk=1).is_money)
        self.assertTrue(CleaningType.objects.get(pk=2).is_money)
        self.assertTrue(CleaningType.objects.get(pk=3).is_money)
        self.assertTrue(CleaningType.objects.get(pk=4).is_money)
        self.assertTrue(CleaningType.objects.get(pk=5).is_money)
        self.assertFalse(CleaningType.objects.get(pk=6).is_money)
