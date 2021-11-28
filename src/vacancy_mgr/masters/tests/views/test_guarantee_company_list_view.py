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


class GuaranteeCompanyListViewTest(TestCase):
    """
    保証会社一覧ビューのテスト
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

    def test_get_guarantee_company_list_view(self):
        url = reverse('masters_guarantee_company_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        guarantee_company = response.context['guarantee_companies'].first()
        self.assertEqual(guarantee_company.id, 1)
        self.assertEqual(guarantee_company.name, '全保連')
