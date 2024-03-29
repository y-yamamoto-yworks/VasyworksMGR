"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from enums.models import Existence
import warnings


class ExistenceModelTest(TestCase):
    """
    有無モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_exists(self):
        self.assertFalse(Existence.objects.get(pk=0).is_exists)
        self.assertTrue(Existence.objects.get(pk=1).is_exists)
        self.assertFalse(Existence.objects.get(pk=2).is_exists)

    def test_is_none(self):
        self.assertFalse(Existence.objects.get(pk=0).is_none)
        self.assertFalse(Existence.objects.get(pk=1).is_none)
        self.assertTrue(Existence.objects.get(pk=2).is_none)
