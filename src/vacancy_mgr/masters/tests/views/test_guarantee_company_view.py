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


class GuaranteeCompanyViewTest(TestCase):
    """
    保証会社ビューのテスト
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

    def test_get_guarantee_company_view(self):
        url = reverse(
            'masters_guarantee_company',
            args=['MQ'],  # 全保連
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        guarantee_company = response.context['guarantee_company']
        self.assertEqual(guarantee_company.name, '全保連')

    def test_post_guarantee_company_view(self):
        url = reverse(
            'masters_guarantee_company',
            args=['MQ'],  # 全保連
        )
        response = self.client.post(
            url,
            {
                'name': '保証会社編集テスト',
                'priority': '10',
                'is_stopped': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
