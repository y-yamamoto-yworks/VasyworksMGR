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
import datetime


class CreateBuildingViewTest(TestCase):
    """
    建物作成ビューのテスト
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

    def test_post_create_building_view(self):
        url = reverse('property_create_building')
        building_name = '建物生成テスト' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        response = self.client.post(
            url,
            {
                'building_name': building_name,
                'building_kana': 'タテモノセイセイテスト',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['default_building_name'], building_name)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '追加しました。')
