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


class CreateRoomVacancyThemeViewTest(TestCase):
    """
    部屋空室テーマ作成ビューのテスト
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

    def test_get_create_room_vacancy_theme_view(self):
        url = reverse(
            'property_create_room_vacancy_theme',
            args=['ccac86695f1d4daaa499c38e871f3d52'],     # サンプルマンション 101号室
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        room = response.context['room']
        self.assertEqual(room.building.building_name, 'サンプルマンション')
        self.assertEqual(room.room_no, '101')

    def test_post_create_room_vacancy_theme_view(self):
        url = reverse(
            'property_create_room_vacancy_theme',
            args=['ccac86695f1d4daaa499c38e871f3d52'],     # サンプルマンション 101号室
        )

        response = self.client.post(
            url,
            {
                'vacancy_theme': '1',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '追加しました。')
