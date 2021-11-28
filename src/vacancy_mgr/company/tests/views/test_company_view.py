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


class CompanyViewTest(TestCase):
    """
    会社ビューのテスト
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

    def test_get_company_view(self):
        url = reverse('company_index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        company = response.context['company']
        self.assertEqual(company.company_name, 'ワイワークス不動産')

    def test_post_company_view(self):
        url = reverse('company_index')
        response = self.client.post(
            url,
            {
                'company_name': '会社編集テスト',
                'company_kana': 'カイシャヘンシュウテスト',
                'shop_name': '会社テスト',
                'api_key': '107a0f11c12c465891ab47b39ea15e30',
                'internal_api_key': '888e953e83f84c659412fe34416d22e4',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
