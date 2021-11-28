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


class DepartmentListViewTest(TestCase):
    """
    部署一覧ビューのテスト
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

    def test_get_department_list_view(self):
        url = reverse('company_department_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        department = response.context['departments'].first()
        self.assertEqual(department.id, 2)
        self.assertEqual(department.department_name, '賃貸管理部')

    def test_get_all_department_list_view(self):
        url = reverse('company_all_department_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
