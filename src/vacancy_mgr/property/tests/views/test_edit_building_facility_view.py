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


class EditBuildingFacilityViewTest(TestCase):
    """
    建物周辺施設編集ビューのテスト
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

    def test_get_edit_building_facility_view(self):
        url = reverse(
            'property_edit_building_facility',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                '2',        # コンビニDEMO
            ],
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        facility = response.context['data']
        self.assertEqual(facility.facility_name, 'コンビニDEMO')

    def test_post_edit_building_facility_view(self):
        url = reverse(
            'property_edit_building_facility',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                '2',  # コンビニDEMO
            ],
        )
        response = self.client.post(
            url,
            {
                'facility_name': '建物周辺施設編集テスト',
                'distance': '1000',
                'priority': '10',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
