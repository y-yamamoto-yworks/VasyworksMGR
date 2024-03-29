"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from enums.models import PaymentFeeType
import warnings


class PaymentFeeTypeModelTest(TestCase):
    """
    支払手数料種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_money(self):
        self.assertFalse(PaymentFeeType.objects.get(pk=0).is_money)
        self.assertTrue(PaymentFeeType.objects.get(pk=10).is_money)
        self.assertTrue(PaymentFeeType.objects.get(pk=20).is_money)
        self.assertTrue(PaymentFeeType.objects.get(pk=30).is_money)
