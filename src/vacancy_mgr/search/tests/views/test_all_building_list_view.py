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


class AllBuildingListViewTest(TestCase):
    """
    全建物一覧ビューのテスト
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

    def test_get_all_building_list_view(self):
        url = reverse('search_buildings_all')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        building = response.context['buildings'][0]
        self.assertEqual(building.building_name, 'サンプルマンション')

    def test_post_all_building_list_view(self):
        url = reverse('search_buildings_all')
        response = self.client.post(
            url,
            {
                'building_name': '表示項目確認',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        building = response.context['buildings'][0]
        self.assertEqual(building.building_name, '表示項目確認用マンション')
