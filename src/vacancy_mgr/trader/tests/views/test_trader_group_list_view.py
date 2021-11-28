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


class TraderGroupListViewTest(TestCase):
    """
    賃貸管理業者グループ一覧ビューのテスト
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

    def test_get_trader_group_list_view(self):
        url = reverse('trader_trader_group_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        trader_group = response.context['trader_groups'].first()
        self.assertEqual(trader_group.id, 1)
        self.assertEqual(trader_group.trader_group_name, 'DEMOホールディングス')

    def test_get_all_trader_group_list_view(self):
        url = reverse('trader_all_trader_group_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
