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


class JuniorHighSchoolViewSetTest(TestCase):
    """
    中学校ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_junior_high_school_view_set(self):
        url = reverse(
            'api_junior_high_schools',
            args=[
                ApiHelper.get_key(),
                '26101',        # 京都市北区
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        school = response.data[0]
        self.assertEqual(school['name'], '旭丘')
