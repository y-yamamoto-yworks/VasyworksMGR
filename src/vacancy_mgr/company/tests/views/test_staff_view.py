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


class StaffViewTest(TestCase):
    """
    スタッフビューのテスト
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

    def test_get_department_view(self):
        url = reverse(
            'company_staff',
            args=['Mg'],  # 管理 太郎
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        staff = response.context['staff']
        self.assertEqual(staff.full_name, '管理 太郎')

    def test_post_department_view(self):
        url = reverse(
            'company_staff',
            args=['Mg'],  # 管理 太郎
        )
        response = self.client.post(
            url,
            {
                'last_name': 'テスト',
                'first_name': 'スタッフ編集',
                'priority': '0',
                'department': '2',
                'is_pm_staff': 'on',
                'is_publish_vacancy': 'on',
                'is_stopped': 'off',
                'is_deleted': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
