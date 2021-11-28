"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.test import Client
from django.urls import reverse
from django.db import transaction
import warnings


class EditRoomViewTest(TestCase):
    """
    部屋編集ビューのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        if transaction.get_autocommit():
            transaction.set_autocommit(False)

        response = self.client.post(
            reverse('login'),
            {'username': 't-kanri', 'password': 'guest1234', },
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        transaction.rollback()

    def test_get_edit_room_view(self):
        url = reverse(
            'property_edit_room',
            args=['5073ab83b3204160a947d1ab470a0b2b'],     # 表示項目確認用マンション DEMO1号室
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        room = response.context['room']
        self.assertEqual(room.building.building_name, '表示項目確認用マンション')
        self.assertEqual(room.room_no, 'DEMO1')

    def test_post_edit_room_view(self):
        url = reverse(
            'property_edit_room',
            args=['5073ab83b3204160a947d1ab470a0b2b'],     # 表示項目確認用マンション DEMO1号室
        )
        response = self.client.post(
            url,
            {
                'room_no': 'TEST',
                'room_floor': '1',
                'rental_type': '0',
                'room_auth_level': '0',
                'is_sublease': 'off',
                'is_entrusted': 'off',
                'is_condo_management': 'off',
                'condo_owner': '0',
                'condo_trader': '0',
                'room_status': '0',
                'vacancy_status': '0',
                'live_start_year': '0',
                'live_start_month': '0',
                'live_start_day': '0',
                'cancel_scheduled_year': '0',
                'cancel_scheduled_month': '0',
                'cancel_scheduled_day': '0',
                'is_publish_vacancy': 'off',
                'is_publish_web': 'off',
                'layout_type': '0',
                'western_style_room1': '0',
                'western_style_room2': '0',
                'western_style_room3': '0',
                'western_style_room4': '0',
                'western_style_room5': '0',
                'western_style_room6': '0',
                'western_style_room7': '0',
                'western_style_room8': '0',
                'western_style_room9': '0',
                'western_style_room10': '0',
                'japanese_style_room1': '0',
                'japanese_style_room2': '0',
                'japanese_style_room3': '0',
                'japanese_style_room4': '0',
                'japanese_style_room5': '0',
                'japanese_style_room6': '0',
                'japanese_style_room7': '0',
                'japanese_style_room8': '0',
                'japanese_style_room9': '0',
                'japanese_style_room10': '0',
                'kitchen_type1': '0',
                'kitchen1': '0',
                'kitchen_type2': '0',
                'kitchen2': '0',
                'kitchen_type3': '0',
                'kitchen3': '0',
                'store_room1': '0',
                'store_room2': '0',
                'store_room3': '0',
                'loft1': '0',
                'loft2': '0',
                'sun_room1': '0',
                'sun_room2': '0',
                'room_area': '0',
                'direction': '0',
                'balcony_type': '0',
                'balcony_area': '0',
                'rent': '0',
                'rent_upper': '0',
                'trader_rent': '0',
                'rent_tax_type': '0',
                'rent_hidden': 'off',
                'condo_fees_type': '0',
                'condo_fees': '0',
                'condo_fees_tax_type': '0',
                'water_cost_type': '0',
                'water_cost': '0',
                'water_cost_tax_type': '0',
                'water_check_type': '0',
                'payment_type': '0',
                'payment_fee_type': '0',
                'payment_fee': '0',
                'payment_fee_tax_type': '0',
                'monthly_cost1': '0',
                'monthly_cost_tax_type1': '0',
                'monthly_cost2': '0',
                'monthly_cost_tax_type2': '0',
                'monthly_cost3': '0',
                'monthly_cost_tax_type3': '0',
                'monthly_cost4': '0',
                'monthly_cost_tax_type4': '0',
                'monthly_cost5': '0',
                'monthly_cost_tax_type5': '0',
                'monthly_cost6': '0',
                'monthly_cost_tax_type6': '0',
                'monthly_cost7': '0',
                'monthly_cost_tax_type7': '0',
                'monthly_cost8': '0',
                'monthly_cost_tax_type8': '0',
                'monthly_cost9': '0',
                'monthly_cost_tax_type9': '0',
                'monthly_cost10': '0',
                'monthly_cost_tax_type10': '0',
                'monthly_cost_note': '0',
                'deposit_type1': '0',
                'deposit_notation1': '0',
                'deposit_value1': '0',
                'deposit_tax_type1': '0',
                'deposit_comment1': '0',
                'deposit_type2': '0',
                'deposit_notation2': '0',
                'deposit_value2': '0',
                'deposit_tax_type2': '0',
                'deposit_comment2': '0',
                'key_money_type1': '0',
                'key_money_notation1': '0',
                'key_money_value1': '0',
                'key_money_tax_type1': '0',
                'key_money_comment1': '0',
                'key_money_type2': '0',
                'key_money_notation2': '0',
                'key_money_value2': '0',
                'key_money_tax_type2': '0',
                'key_money_comment2': '0',
                'contract_years': '0',
                'contract_months': '0',
                'renewal_fee_notation': '0',
                'renewal_fee_value': '0',
                'renewal_fee_tax_type': '0',
                'renewal_charge_existence': '0',
                'renewal_charge': '0',
                'renewal_charge_tax_type': '0',
                'is_auto_renewal': 'off',
                'recontract_fee_existence': '0',
                'recontract_fee': '0',
                'recontract_fee_tax_type': '0',
                'insurance_type': '0',
                'insurance_years': '0',
                'insurance_fee': '0',
                'insurance_fee_tax_type': '0',
                'guarantee_type': '0',
                'document_cost_existence': '0',
                'document_cost': '0',
                'document_cost_tax_type': '0',
                'key_change_cost_existence': '0',
                'key_change_cost': '0',
                'key_change_cost_tax_type': '0',
                'initial_cost1': '0',
                'initial_cost_tax_type1': '0',
                'initial_cost2': '0',
                'initial_cost_tax_type2': '0',
                'initial_cost3': '0',
                'initial_cost_tax_type3': '0',
                'initial_cost4': '0',
                'initial_cost_tax_type4': '0',
                'initial_cost5': '0',
                'initial_cost_tax_type5': '0',
                'initial_cost6': '0',
                'initial_cost_tax_type6': '0',
                'initial_cost7': '0',
                'initial_cost_tax_type7': '0',
                'initial_cost8': '0',
                'initial_cost_tax_type8': '0',
                'initial_cost9': '0',
                'initial_cost_tax_type9': '0',
                'initial_cost10': '0',
                'initial_cost_tax_type10': '0',
                'free_rent_type': '0',
                'free_rent_months': '0',
                'free_rent_limit_year': '0',
                'free_rent_limit_month': '0',
                'cancel_notice_limit': '0',
                'cleaning_type': '0',
                'cleaning_cost': '0',
                'cleaning_cost_tax_type': '0',
                'electric_type': '0',
                'gas_type': '0',
                'bath_type': '0',
                'toilet_type': '0',
                'kitchen_range_type': '0',
                'internet_type': '0',
                'washer_type': '0',
                'pet_type': '0',
                'instrument_type': '0',
                'live_together_type': '0',
                'children_type': '0',
                'share_type': '0',
                'non_japanese_type': '0',
                'only_woman_type': '0',
                'only_man_type': '0',
                'corp_contract_type': '0',
                'student_type': '0',
                'new_student_type': '0',
                'welfare_type': '0',
                'office_use_type': '0',
                'reform_year': '0',
                'reform_month': '0',
                'trader_publish_type': '0',
                'trader_portal_type': '0',
                'ad_type': '0',
                'ad_value': '0',
                'ad_tax_type': '0',
                'trader_ad_type': '0',
                'trader_ad_value': '0',
                'trader_ad_tax_type': '0',
                'owner_fee_type': '0',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
