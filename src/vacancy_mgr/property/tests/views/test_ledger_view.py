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


class LedgerViewTest(TestCase):
    """
    物件台帳表示ビューのテスト
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

    def test_get_ledger_view(self):
        url = reverse(
            'property_ledger',
            args=['5073ab83b3204160a947d1ab470a0b2b'],     # 表示項目確認用マンション DEMO1号室
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        room = response.context['room']
        self.assertEqual(room.building.building_name, '表示項目確認用マンション')
        self.assertEqual(room.room_no, 'DEMO1')
