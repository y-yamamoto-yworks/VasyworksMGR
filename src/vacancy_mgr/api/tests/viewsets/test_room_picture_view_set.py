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
from api.api_helper import ApiHelper


class RoomPictureViewSetTest(TestCase):
    """
    部屋写真ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_room_picture_view_set(self):
        url = reverse(
            'api_room_pictures',
            args=[
                ApiHelper.get_key(),
                3,        # 表示項目確認用マンション DEMO01号室
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        room_picture = response.data[0]
        self.assertEqual(room_picture['comment'], '間取図画像コメントDEMOデータ')
