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


class VacancyUserListViewTest(TestCase):
    """
    空室情報閲覧ユーザー一覧ビューのテスト
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

    def test_get_vacancy_user_list_view(self):
        url = reverse('users_vacancy_user_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        user = response.context['users'].first()
        self.assertEqual(user.username, 'a-pool')
        self.assertEqual(user.display_name, 'エイプール')

    def test_post_vacancy_user_list_view(self):
        url = reverse('users_vacancy_user_list')
        response = self.client.post(
            url,
            {
                'display_name': 'ワイワークス',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        user = response.context['users'].first()
        self.assertEqual(user.username, 'yworks')
        self.assertEqual(user.display_name, 'ワイワークス不動産')

    def test_get_all_vacancy_user_list_view(self):
        url = reverse('users_all_vacancy_user_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
