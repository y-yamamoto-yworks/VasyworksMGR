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


class VacancyThemeViewTest(TestCase):
    """
    空室テーマビューのテスト
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

    def test_get_vacancy_theme_view(self):
        url = reverse(
            'vacancy_item_vacancy_theme',
            args=['MQ'],  # オススメ
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        vacancy_theme = response.context['vacancy_theme']
        self.assertEqual(vacancy_theme.name, 'オススメ')

    def test_post_vacancy_theme_view(self):
        url = reverse(
            'vacancy_item_vacancy_theme',
            args=['MQ'],  # オススメ
        )
        response = self.client.post(
            url,
            {
                'name': 'テスト',
                'title': '空室テーマ編集テスト',
                'priority': '10',
                'room_auth_level': '0',
                'is_publish': 'on',
                'is_stopped': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
