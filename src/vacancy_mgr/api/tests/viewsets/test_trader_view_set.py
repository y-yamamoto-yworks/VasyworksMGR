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
from api.api_helper import ApiHelper


class TraderViewSetTest(TestCase):
    """
    賃貸管理業者ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_trader_view_set(self):
        url = reverse(
            'api_traders',
            args=[
                ApiHelper.get_key(),
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        trader = response.data[0]
        self.assertEqual(trader['trader_name'], '賃貸ライフ')

    def test_get_trader_with_hint_view_set(self):
        url = reverse(
            'api_traders_with_hint',
            args=[
                ApiHelper.get_key(),
                'ライフ',
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        trader = response.data[0]
        self.assertEqual(trader['trader_name'], '賃貸ライフ')
