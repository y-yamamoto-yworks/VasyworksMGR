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


class UserListViewTest(TestCase):
    """
    ユーザー一覧ビューのテスト
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

    def test_get_user_list_view(self):
        url = reverse('users_user_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        user = response.context['users'].first()
        self.assertEqual(user.username, 'i-chintai')
        self.assertEqual(user.full_name, '賃貸 一郎')

    def test_get_all_user_list_view(self):
        url = reverse('users_all_user_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
