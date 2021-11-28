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


class CreateUserViewTest(TestCase):
    """
    ユーザー作成ビューのテスト
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

    def test_post_create_user_view(self):
        url = reverse('users_create_user')
        response = self.client.post(
            url,
            {
                'username': 'test_user1',
                'password1': 'vasyworks1234',
                'password2': 'vasyworks1234',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '追加しました。')

    def test_post_create_user_view_with_staff(self):
        url = reverse('users_create_user')
        url += 'NA'        # DEMOスタッフ
        response = self.client.post(
            url,
            {
                'username': 'test_user2',
                'password1': 'vasyworks1234',
                'password2': 'vasyworks1234',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '追加しました。')
