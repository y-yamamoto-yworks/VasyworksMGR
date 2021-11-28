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


class TraderGroupViewTest(TestCase):
    """
    賃貸管理業者グループビューのテスト
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

    def test_get_trader_view(self):
        url = reverse(
            'trader_trader_group',
            args=['MQ'],  # DEMOホールディングス
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        trader_group = response.context['trader_group']
        self.assertEqual(trader_group.trader_group_name, 'DEMOホールディングス')

    def test_post_owner_view(self):
        url = reverse(
            'trader_trader_group',
            args=['MQ'],  # DEMOホールディングス
        )
        response = self.client.post(
            url,
            {
                'trader_group_name': '賃貸管理業者グループ編集テスト',
                'trader_group_kana': 'チンタイカンリギョウシャグループヘンシュウテスト',
                'is_stopped': 'off',
                'is_deleted': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
