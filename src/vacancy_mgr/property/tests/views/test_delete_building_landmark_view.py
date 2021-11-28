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


class DeleteBuildingLandmarkViewTest(TestCase):
    """
    建物ランドマーク削除ビューのテスト
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

    def test_get_delete_building_landmark_view(self):
        url = reverse(
            'property_delete_building_landmark',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                2,           # 京都府立大学
            ],
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        landmark = response.context['data']
        self.assertEqual(landmark.landmark.name, '京都府立大学')

    def test_post_delete_building_landmark_view(self):
        url = reverse(
            'property_delete_building_landmark',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                2,           # 京都府立大学
            ],
        )

        response = self.client.post(
            url,
            {
                'confirm': 'on',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '削除しました。')
