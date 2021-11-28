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


class CopyRoomPictureViewTest(TestCase):
    """
    部屋画像コピービューのテスト
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

    def test_get_copy_room_picture_view(self):
        url = reverse(
            'property_copy_room_picture',
            args=[
                'ba86aedf28f24ec99117257aa155063b',     # 表示項目確認用マンション DEMO2号室
            ],
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        room = response.context['room']
        self.assertEqual(room.building.building_name, '表示項目確認用マンション')
        self.assertEqual(room.room_no, 'DEMO2')

    def test_post_copy_room_picture_view(self):
        url = reverse(
            'property_copy_room_picture',
            args=[
                'ba86aedf28f24ec99117257aa155063b',     # 表示項目確認用マンション DEMO2号室
            ],
        )

        response = self.client.post(
            url,
            {
                'selected_room': '3',       # DEMO1号室
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '画像をコピーしました。')
