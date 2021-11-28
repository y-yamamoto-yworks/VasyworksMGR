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


class VacancyInputBikeParkingListViewTest(TestCase):
    """
    空室入力駐輪場一覧ビューのテスト
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

    def test_get_vacancy_input_bike_parking_list_view(self):
        url = reverse('vacancy_item_vacancy_input_bike_parking_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        item = response.context['items'].first()
        self.assertEqual(item.id, 1)
        self.assertEqual(item.input_contents, '無し')
