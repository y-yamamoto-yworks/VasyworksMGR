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


class EditBuildingViewTest(TestCase):
    """
    建物編集ビューのテスト
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

    def test_get_edit_building_view(self):
        url = reverse(
            'property_edit_building',
            args=['98d6c2ccd9384062ab5fb4dd61b3e8fc'],     # 表示項目確認用マンション
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        building = response.context['building']
        self.assertEqual(building.building_name, '表示項目確認用マンション')

    def test_post_edit_building_view(self):
        url = reverse(
            'property_edit_building',
            args=['98d6c2ccd9384062ab5fb4dd61b3e8fc'],     # 表示項目確認用マンション
        )
        response = self.client.post(
            url,
            {
                'building_name': '建物編集テスト',
                'building_kana': 'タテモノヘンシュウテスト',
                'pref': '0',
                'city': '0',
                'area': '0',
                'elementary_school': '0',
                'elementary_school_distance': '0',
                'junior_high_school': '0',
                'junior_high_school_distance': '0',
                'management_type': '0',
                'department': '0',
                'staff1': '0',
                'staff2': '0',
                'priority_level': '0',
                'agency_department': '0',
                'owner': '0',
                'trader': '0',
                'arrival_type1': '0',
                'station1': '0',
                'station_time1': '0',
                'bus_stop_time1': '0',
                'arrival_type2': '0',
                'station2': '0',
                'station_time2': '0',
                'bus_stop_time2': '0',
                'arrival_type3': '0',
                'station3': '0',
                'station_time3': '0',
                'bus_stop_time3': '0',
                'building_type': '0',
                'structure': '0',
                'building_rooms': '0',
                'building_floors': '0',
                'building_undergrounds': '0',
                'build_year': '0',
                'build_month': '0',
                'bike_parking_type': '0',
                'with_bike_parking_roof': 'off',
                'bike_parking_fee_lower': '0',
                'bike_parking_fee_upper': '0',
                'bike_parking_fee_tax_type': '0',
                'garage_type': '0',
                'garage_status': '0',
                'garage_distance': '0',
                'garage_fee_lower': '0',
                'garage_fee_upper': '0',
                'garage_fee_tax_type': '0',
                'garage_charge_lower': '0',
                'garage_charge_upper': '0',
                'garage_charge_tax_type': '0',
                'agreement_existence': '0',
                'is_hidden_vacancy': 'off',
                'is_vacancy_recommend': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
