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


class DepartmentViewSetTest(TestCase):
    """
    部署ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_department_view_set(self):
        url = reverse(
            'api_departments',
            args=[
                ApiHelper.get_key(),
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        department = response.data[0]
        self.assertEqual(department['department_name'], '賃貸管理部')

    def test_get_department_with_hint_view_set(self):
        url = reverse(
            'api_departments_with_hint',
            args=[
                ApiHelper.get_key(),
                '管理',
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        department = response.data[0]
        self.assertEqual(department['department_name'], '賃貸管理部')
