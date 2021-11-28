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


class InsuranceCompanyViewSetTest(TestCase):
    """
    火災保険会社ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()

    def test_get_insurance_company_view_set(self):
        url = reverse(
            'api_insurance_company',
            args=[
                ApiHelper.get_key(),
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        insurance_company = response.data[0]
        self.assertEqual(insurance_company['name'], '損保ジャパン')
