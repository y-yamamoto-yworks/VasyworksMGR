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


class VacancyInputInternetViewSetTest(TestCase):
    """
    空室情報入力（インターネット）ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_vacancy_input_internet_view_set(self):
        url = reverse(
            'api_vacancy_input_internets',
            args=[
                ApiHelper.get_key(),
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        item = response.data[0]
        self.assertEqual(item['input_contents'], 'インターネット無料')