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


class EditBuildingPictureViewTest(TestCase):
    """
    建物画像編集ビューのテスト
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

    def test_get_edit_building_picture_view(self):
        url = reverse(
            'property_edit_building_picture',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                3,           # 建物外観
            ],
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        picture = response.context['data']
        self.assertEqual(picture.picture_type.name, '建物外観')

    def test_post_edit_building_picture_view(self):
        url = reverse(
            'property_edit_building_picture',
            args=[
                '98d6c2ccd9384062ab5fb4dd61b3e8fc',     # 表示項目確認用マンション
                3,           # 建物外観
            ],
        )
        response = self.client.post(
            url,
            {
                'picture_type': '1020',
                'priority': '0',
                'is_publish_web': 'on',
                'is_publish_vacancy': 'on',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
