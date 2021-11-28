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


class EditManagementInfoViewTest(TestCase):
    """
    管理お知らせビューのテスト
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

    def test_get_edit_management_info_view(self):
        url = reverse(
            'info_edit_management_info',
            args=['Mw'],    # 管理お知らせDEMOデータ3
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        info = response.context['info']
        self.assertEqual(info.information, '管理お知らせDEMOデータ3')

    def test_post_edit_management_info_view(self):
        url = reverse(
            'info_edit_management_info',
            args=['Mw'],    # 管理お知らせDEMOデータ3
        )
        response = self.client.post(
            url,
            {
                'information': '管理お知らせ編集テスト',
                'start_date': '2020-01-01',
                'end_date': '2020-12-31',
                'is_emphasized': 'off',
                'priority': '10',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
