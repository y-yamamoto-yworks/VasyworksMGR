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


class VacancyUserViewTest(TestCase):
    """
    空室情報閲覧ユーザービューのテスト
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

    def test_get_vacancy_user_view(self):
        url = reverse(
            'users_vacancy_user',
            args=['MQ'],  # ワイワークス不動産
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        target_user = response.context['target_user']
        self.assertEqual(target_user.display_name, 'ワイワークス不動産')

    def test_post_vacancy_user_view(self):
        url = reverse(
            'users_vacancy_user',
            args=['MQ'],  # ワイワークス不動産
        )
        response = self.client.post(
            url,
            {
                'username': 'test-user',
                'display_name': '空室情報閲覧ユーザ編集テスト',
                'is_active': 'on',
                'is_company': 'on',
                'level': '0',
                'allow_org_image': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
