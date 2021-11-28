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


class OwnerViewSetTest(TestCase):
    """
    オーナービューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_owner_view_set(self):
        url = reverse(
            'api_owners',
            args=[
                ApiHelper.get_key(),
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        owner = response.data[0]
        self.assertEqual(owner['owner_name'], '一条　剣之介')

    def test_get_owner_with_hint_view_set(self):
        url = reverse(
            'api_owners_with_hint',
            args=[
                ApiHelper.get_key(),
                '一条',
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        owner = response.data[0]
        self.assertEqual(owner['owner_name'], '一条　剣之介')
