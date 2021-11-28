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


class StaffViewSetTest(TestCase):
    """
    スタッフビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_staff_view_set(self):
        url = reverse(
            'api_staffs',
            args=[
                ApiHelper.get_key(),
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        staff = response.data[0]
        self.assertEqual(staff['full_name'], '管理 太郎')

    def test_get_staff_with_hint_view_set(self):
        url = reverse(
            'api_staffs_with_hint',
            args=[
                ApiHelper.get_key(),
                '管理',
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        staff = response.data[0]
        self.assertEqual(staff['full_name'], '管理 太郎')
