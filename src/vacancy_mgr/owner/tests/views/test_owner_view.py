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


class OwnerViewTest(TestCase):
    """
    オーナービューのテスト
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

    def test_get_owner_view(self):
        url = reverse(
            'owner_detail',
            args=['Mw'],  # 一条　剣之介
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        owner = response.context['owner']
        self.assertEqual(owner.owner_name, '一条　剣之介')

    def test_post_owner_view(self):
        url = reverse(
            'owner_detail',
            args=['Mw'],  # 一条　剣之介
        )
        response = self.client.post(
            url,
            {
                'owner_name': 'オーナー編集テスト',
                'owner_kana': 'オーナーヘンシュウテスト',
                'is_corporation': 'off',
                'staff': '0',
                'is_stopped': 'off',
                'is_deleted': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
