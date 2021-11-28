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


class EditRoomMovieViewTest(TestCase):
    """
    部屋動画編集ビューのテスト
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

    def test_get_edit_room_movie_view(self):
        url = reverse(
            'property_edit_room_movie',
            args=[
                '5073ab83b3204160a947d1ab470a0b2b',     # 表示項目確認用マンション DEMO1号室
                35,           # 室内
            ],
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        movie = response.context['data']
        self.assertEqual(movie.movie_type.name, '室内')

    def test_post_edit_room_movie_view(self):
        url = reverse(
            'property_edit_room_movie',
            args=[
                '5073ab83b3204160a947d1ab470a0b2b',     # 表示項目確認用マンション DEMO1号室
                35,           # 室内
            ],
        )
        response = self.client.post(
            url,
            {
                'movie_type': '2020',
                'priority': '0',
                'is_publish_web': 'on',
                'is_publish_vacancy': 'on',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
