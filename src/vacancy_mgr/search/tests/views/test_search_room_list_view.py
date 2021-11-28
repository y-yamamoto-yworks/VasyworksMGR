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


class SearchRoomListViewTest(TestCase):
    """
    部屋検索ビューのテスト
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

    def test_get_search_room_list_view(self):
        url = reverse('search_rooms')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_post_search_room_list_view(self):
        url = reverse('search_rooms')
        response = self.client.post(
            url,
            {
                'building_is_hidden_vacancy': '0',
                'building_is_vacancy_recommend': '0',
                'building_is_hidden_web': '0',
                'is_sublease': '0',
                'is_condo_management': '0',
                'is_entrusted': '0',
                'room_status_category': '10',
                'room_is_publish_vacancy': '0',
                'room_is_publish_web': '0',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        room = response.context['rooms'][0]
        self.assertEqual(room.building.building_name, 'サンプルマンション')
        self.assertEqual(room.room_no, '101')

    def test_post_search_room_list_view_with_upper_rent(self):
        url = reverse('search_rooms')
        response = self.client.post(
            url,
            {
                'upper_rent': '50000',
                'building_is_hidden_vacancy': '0',
                'building_is_vacancy_recommend': '0',
                'building_is_hidden_web': '0',
                'is_sublease': '0',
                'is_condo_management': '0',
                'is_entrusted': '0',
                'room_status_category': '10',
                'room_is_publish_vacancy': '0',
                'room_is_publish_web': '0',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        room = response.context['rooms'][0]
        self.assertEqual(room.building.building_name, 'リストサンプルマンション1')
        self.assertEqual(room.room_no, '101')

    def test_post_search_room_list_view_with_lower_rent(self):
        url = reverse('search_rooms')
        response = self.client.post(
            url,
            {
                'lower_rent': '55000',
                'building_is_hidden_vacancy': '0',
                'building_is_vacancy_recommend': '0',
                'building_is_hidden_web': '0',
                'is_sublease': '0',
                'is_condo_management': '0',
                'is_entrusted': '0',
                'room_status_category': '10',
                'room_is_publish_vacancy': '0',
                'room_is_publish_web': '0',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        room = response.context['rooms'][0]
        self.assertEqual(room.building.building_name, 'サンプルマンション')
        self.assertEqual(room.room_no, '101')

    def test_post_search_room_list_view_with_station(self):
        url = reverse('search_rooms')
        response = self.client.post(
            url,
            {
                'station': '1220',      # 地下鉄烏丸線 国際会館
                'building_is_hidden_vacancy': '0',
                'building_is_vacancy_recommend': '0',
                'building_is_hidden_web': '0',
                'is_sublease': '0',
                'is_condo_management': '0',
                'is_entrusted': '0',
                'room_status_category': '10',
                'room_is_publish_vacancy': '0',
                'room_is_publish_web': '0',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        room = response.context['rooms'][0]
        self.assertEqual(room.building.building_name, '分譲賃貸サンプルマンション')
        self.assertEqual(room.room_no, '1001')
