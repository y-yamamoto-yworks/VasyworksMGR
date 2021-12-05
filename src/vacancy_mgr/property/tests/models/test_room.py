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


class RoomModelTest(TestCase):
    """
    部屋モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション
        self.room = self.building.rooms.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_room_other_rooms(self):
        other_rooms = self.room.other_rooms
        for other_room in other_rooms:
            self.assertIsNot(other_room, self.room)

    def test_room_rent_text(self):
        self.assertEqual(self.room.rent_text, '52,000 円 〜 53,000 円')
        self.room.rent_upper = 0
        self.assertEqual(self.room.rent_text, '52,000 円')
        self.room.rent = 0
        self.assertEqual(self.room.rent_text, '0 円')

    def test_room_trader_rent_text(self):
        self.assertEqual(self.room.trader_rent_text, '55,000 円')
        self.room.trader_rent = 0
        self.assertIsNone(self.room.trader_rent_text)

    def test_room_condo_fees_text(self):
        self.assertEqual(self.room.condo_fees_text, '3,000 円')
        self.room.condo_fees_type_id = 20
        self.assertEqual(self.room.condo_fees_text, '込み')
        self.room.condo_fees_type_id = 0
        self.assertEqual(self.room.condo_fees_text, '不明')

    def test_room_water_cost_text(self):
        self.assertEqual(self.room.water_cost_text, '2,000 円（税込）')
        self.room.water_cost_type_id = 10
        self.assertEqual(self.room.water_cost_text, '実費')
        self.room.water_cost_type_id = 0
        self.assertEqual(self.room.water_cost_text, '不明')

    def test_room_payment_fee_text(self):
        self.assertEqual(self.room.payment_fee_text, '振替手数料 300 円（税別）')
        self.room.payment_fee_type_id = 0
        self.assertEqual(self.room.payment_fee_text, '不明')

    def test_room_free_rent_text(self):
        self.assertEqual(self.room.free_rent_text, '有り（月数指定） 1ヶ月')
        self.room.free_rent_type_id = 2
        self.room.free_rent_limit_year = 2021
        self.room.free_rent_limit_month = 5
        self.assertEqual(self.room.free_rent_text, '有り（期限月指定） 2021年5月')
        self.room.free_rent_type_id = 0
        self.assertEqual(self.room.free_rent_text, '無し')

    def test_room_monthly_cost_texts(self):
        self.assertEqual(self.room.monthly_cost_text1, '月額費用DEMO11,000 円(税別)')
        self.assertEqual(self.room.monthly_cost_text2, '月額費用DEMO2500 円(税込)')
        self.assertEqual(self.room.monthly_cost_text3, '月額費用DEMO32,000 円(税別)')
        self.assertIsNone(self.room.monthly_cost_text4)
        self.assertIsNone(self.room.monthly_cost_text5)
        self.assertIsNone(self.room.monthly_cost_text6)
        self.assertIsNone(self.room.monthly_cost_text7)
        self.assertIsNone(self.room.monthly_cost_text8)
        self.assertIsNone(self.room.monthly_cost_text9)
        self.assertIsNone(self.room.monthly_cost_text10)

    def test_room_deposit_texts(self):
        self.room.deposit_notation1_id = 1
        self.assertEqual(self.room.deposit_text1, '敷金 無し')
        self.room.deposit_notation1_id = 2
        self.room.deposit_value1 = 100000
        self.assertEqual(self.room.deposit_text1, '敷金 100,000 円')

        self.assertIsNone(self.room.deposit_text2)
        self.room.deposit_type2_id = 20
        self.room.deposit_notation2_id = 1
        self.assertEqual(self.room.deposit_text2, '保証金 無し')
        self.room.deposit_notation2_id = 2
        self.room.deposit_value2 = 100000
        self.assertEqual(self.room.deposit_text2, '保証金 100,000 円')

    def test_room_key_money_texts(self):
        self.assertEqual(self.room.key_money_text1, '礼金 賃料 1 ヶ月')
        self.room.key_money_notation1_id = 1
        self.assertEqual(self.room.key_money_text1, '礼金 無し')
        self.room.key_money_notation1_id = 2
        self.room.key_money_value1 = 100000
        self.assertEqual(self.room.key_money_text1, '礼金 100,000 円')

        self.assertIsNone(self.room.key_money_text2)
        self.room.key_money_type2_id = 20
        self.room.key_money_notation2_id = 1
        self.assertEqual(self.room.key_money_text2, '解約引 無し')
        self.room.key_money_notation2_id = 2
        self.room.key_money_value2 = 100000
        self.assertEqual(self.room.key_money_text2, '解約引 100,000 円')

    def test_room_insurance_text(self):
        self.assertEqual(self.room.insurance_text, '自社指定 部屋火災保険会社DEMO 2年 15,000 円（税込）')
        self.room.insurance_type_id = 3
        self.assertEqual(self.room.insurance_text, '推奨')

    def test_room_document_cost_text(self):
        self.assertEqual(self.room.document_cost_text, '8,000 円（税込）')
        self.room.document_cost_existence_id = 2
        self.assertIsNone(self.room.document_cost_text)

    def test_room_key_change_cost_text(self):
        self.assertEqual(self.room.key_change_cost_text, '15,000 円（税別）')
        self.room.key_change_cost_existence_id = 2
        self.assertEqual(self.room.key_change_cost_text, None)

    def test_room_initial_cost_texts(self):
        self.assertEqual(self.room.initial_cost_text1, '初期費用DEMO15,000 円(税別)')
        self.assertEqual(self.room.initial_cost_text2, '初期費用DEMO210,000 円(税別)')
        self.assertEqual(self.room.initial_cost_text3, '初期費用DEMO3500 円(税別)')
        self.assertIsNone(self.room.initial_cost_text4)
        self.assertIsNone(self.room.initial_cost_text5)
        self.assertIsNone(self.room.initial_cost_text6)
        self.assertIsNone(self.room.initial_cost_text7)
        self.assertIsNone(self.room.initial_cost_text8)
        self.assertIsNone(self.room.initial_cost_text9)
        self.assertIsNone(self.room.initial_cost_text10)

    def test_room_contract_span_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.contract_span_text, '2年')
        room.contract_years = 0
        room.contract_months = 0
        self.assertIsNone(room.contract_span_text)
        room.contract_months = 10
        self.assertEqual(room.contract_span_text, '10ヶ月')
        room.contract_years = 1
        room.contract_months = 6
        self.assertEqual(room.contract_span_text, '1年6ヶ月')

    def test_room_renewal_fee_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.renewal_fee_text, '新賃料の 1 ヶ月')
        room.renewal_fee_notation_id = 1
        self.assertEqual(room.renewal_fee_text, '無し')
        room.renewal_fee_notation_id = 2
        room.renewal_fee_value = 50000
        self.assertEqual(room.renewal_fee_text, '50,000 円')

    def test_room_renewal_charge_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.renewal_charge_text, '10,000 円（税別）')
        room.renewal_charge_existence_id = 2
        self.assertIsNone(room.renewal_charge_text)

    def test_room_recontract_fee_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertIsNone(room.recontract_fee_text)
        room.recontract_fee_existence_id = 1
        room.recontract_fee = 33000
        room.recontract_fee_tax_type_id = 2
        self.assertEqual(room.recontract_fee_text, '33,000 円（税込）')

    def test_room_cancel_notice_limit_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.cancel_notice_limit_text, '解約予定日の2ヶ月前')
        room.cancel_notice_limit = 0
        self.assertIsNone(room.cancel_notice_limit_text)

    def test_room_cleaning_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.cleaning_text, '敷金相殺15,000 円（税別）')
        room.cleaning_type_id = 0
        self.assertEqual(room.cleaning_text, '不明')

    def test_room_condo_management_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertIsNone(room.condo_management_text)
        building.management_type_id = 30
        room.is_sublease = 1
        room.is_entrusted = 0
        room.is_condo_management = 0
        self.assertEqual(room.condo_management_text, '部屋一室借上')
        room.is_sublease = 0
        room.is_entrusted = 1
        room.is_condo_management = 0
        self.assertEqual(room.condo_management_text, '部屋一室専任')
        room.is_sublease = 0
        room.is_entrusted = 0
        room.is_condo_management = 1
        self.assertEqual(room.condo_management_text, '分譲管理')
        room.is_sublease = 0
        room.is_entrusted = 0
        room.is_condo_management = 0
        self.assertEqual(room.condo_management_text, '分譲管理外')

    def test_room_area_texts(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.room_area_text, '40.55')
        self.assertEqual(room.balcony_area_text, '7')

    def test_room_layout_detail_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.layout_detail_text, '洋6帖×和6帖×DK4.5帖')

    def test_room_ad_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertEqual(room.ad_text, '賃料の 1 ヶ月（税別）')
        room.ad_type_id = 2
        room.ad_value = 55000
        room.ad_tax_type_id = 2
        self.assertEqual(room.ad_text, '55,000 円（税込）')
        room.ad_type_id = 1
        self.assertEqual(room.ad_text, '無し')
        room.ad_type_id = 0
        self.assertEqual(room.ad_text, '不明')

    def test_room_trader_ad_text(self):
        building = Building.objects.get(pk=2)  # 表示項目確認用マンション
        room = building.rooms.first()
        self.assertIsNone(room.trader_ad_text)
        room.trader_ad_type_id = 3
        room.trader_ad_value = 0.5
        room.trader_ad_tax_type_id = 1
        self.assertEqual(room.trader_ad_text, '賃料の 0.5 ヶ月（税別）')
        room.trader_ad_type_id = 2
        room.trader_ad_value = 44000
        room.trader_ad_tax_type_id = 2
        self.assertEqual(room.trader_ad_text, '44,000 円（税込）')
        room.trader_ad_type_id = 1
        self.assertEqual(room.trader_ad_text, '無し')
        room.trader_ad_type_id = 0
        self.assertIsNone(room.trader_ad_text)
