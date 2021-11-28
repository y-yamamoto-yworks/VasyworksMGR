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


class PostalCodeViewSetTest(TestCase):
    """
    郵便番号ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_postal_code_view_set(self):
        url = reverse(
            'api_postal_code',
            args=[
                ApiHelper.get_key(),
                '602-0831',        # 立本寺前町
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['town_name'], '立本寺前町')
