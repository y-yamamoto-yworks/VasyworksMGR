"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from property.models import Building, BuildingGarage
import warnings


class BuildingGarageModelTest(TestCase):
    """
    建物駐車場モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション
        self.garage = self.building.building_garages.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_garage_garage_fee_text(self):
        self.assertEqual(self.garage.garage_fee_text, '10,000 円（税別）')
        self.garage.garage_fee = 0
        self.assertIsNone(self.garage.garage_fee_text)

    def test_building_garage_garage_charge_text(self):
        self.assertEqual(self.garage.garage_charge_text, '5,000 円（税別）')
        self.garage.garage_charge = 0
        self.assertIsNone(self.garage.garage_charge_text)

    def test_building_garage_garage_deposit_text(self):
        self.assertEqual(self.garage.garage_deposit_text, '10,000 円（税別）')
        self.garage.garage_deposit = 0
        self.assertIsNone(self.garage.garage_deposit_text)

    def test_building_garage_certification_fee_text(self):
        self.assertEqual(self.garage.certification_fee_text, '6,000 円（税別）')
        self.garage.certification_fee = 0
        self.assertIsNone(self.garage.certification_fee_text)
