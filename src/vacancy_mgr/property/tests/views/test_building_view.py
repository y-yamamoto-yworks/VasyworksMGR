"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.test import Client
from django.urls import reverse
import warnings


class BuildingViewTest(TestCase):
    """
    建物ビューのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

        response = self.client.post(
            reverse('login'),
            {'username': 't-kanri', 'password': 'guest1234', },
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_get_building_view(self):
        url = reverse(
            'property_building',
            args=['98d6c2ccd9384062ab5fb4dd61b3e8fc'],     # 表示項目確認用マンション
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        building = response.context['building']
        self.assertEqual(building.id, 2)
        self.assertEqual(building.building_name, '表示項目確認用マンション')
        room = building.rooms.first()
        self.assertEqual(room.id, 3)
        self.assertEqual(room.room_no, 'DEMO1')
