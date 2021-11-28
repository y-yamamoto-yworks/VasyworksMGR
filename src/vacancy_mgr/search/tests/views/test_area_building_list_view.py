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


class AreaBuildingListViewTest(TestCase):
    """
    建物エリア検索ビューのテスト
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

    def test_get_area_building_list_view(self):
        url = reverse('search_buildings_area')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_post_area_building_list_view(self):
        url = reverse('search_buildings_area')
        response = self.client.post(
            url,
            {
                'pref': '26',
                'city': '26104',    # 京都市中京区
                'area': '26049',    # 烏丸
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        building = response.context['buildings'][0]
        self.assertEqual(building.building_name, 'リストサンプルマンション1')

    def test_post_area_building_list_view_without_area(self):
        url = reverse('search_buildings_area')
        response = self.client.post(
            url,
            {
                'pref': '26',
                'city': '26101',    # 京都市北区
                'area': '0',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        building = response.context['buildings'][0]
        self.assertEqual(building.building_name, 'サンプルマンション')
