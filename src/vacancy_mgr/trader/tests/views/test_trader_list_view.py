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


class TraderListViewTest(TestCase):
    """
    賃貸管理業者一覧ビューのテスト
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

    def test_get_trader_list_view(self):
        url = reverse('trader_trader_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        trader = response.context['traders'].first()
        self.assertEqual(trader.id, 1)
        self.assertEqual(trader.trader_name, '賃貸ライフ')

    def test_post_trader_list_view(self):
        url = reverse('trader_trader_list')
        response = self.client.post(
            url,
            {
                'trader_name': 'DEMO',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        trader = response.context['traders'].first()
        self.assertEqual(trader.id, 2)
        self.assertEqual(trader.trader_name, 'DEMO不動産')

    def test_get_all_trader_list_view(self):
        url = reverse('trader_all_trader_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
