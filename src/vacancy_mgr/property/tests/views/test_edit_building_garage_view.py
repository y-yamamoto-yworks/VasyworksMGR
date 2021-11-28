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


class EditBuildingGarageViewTest(TestCase):
    """
    建物駐車場編集ビューのテスト
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

    def test_get_edit_building_garage_view(self):
        url = reverse(
            'property_edit_building_garage',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                '3',        # DEMO01
            ],
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        garage = response.context['data']
        self.assertEqual(garage.garage_name, 'DEMO01')

    def test_post_edit_building_garage_view(self):
        url = reverse(
            'property_edit_building_garage',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                '3',        # DEMO01
            ],
        )
        response = self.client.post(
            url,
            {
                'garage_name': '建物駐車場編集テスト',
                'garage_status': '0',
                'priority': '0',
                'garage_fee': '0',
                'garage_fee_tax_type': '0',
                'garage_charge': '0',
                'garage_charge_tax_type': '0',
                'garage_deposit': '0',
                'garage_deposit_tax_type': '0',
                'certification_fee': '0',
                'certification_fee_tax_type': '0',
                'initial_cost1': '0',
                'initial_cost_tax_type1': '0',
                'initial_cost2': '0',
                'initial_cost_tax_type2': '0',
                'initial_cost3': '0',
                'initial_cost_tax_type3': '0',
                'allow_no_room': 'off',
                'width': '0',
                'length': '0',
                'height': '0',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
