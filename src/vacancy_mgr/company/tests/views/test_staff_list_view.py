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


class StaffListViewTest(TestCase):
    """
    スタッフ一覧ビューのテスト
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

    def test_get_staff_list_view(self):
        url = reverse('company_staff_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        staff = response.context['staffs'].first()
        self.assertEqual(staff.id, 2)
        self.assertEqual(staff.full_name, '管理 太郎')

    def test_post_staff_list_view(self):
        url = reverse('company_staff_list')
        response = self.client.post(
            url,
            {
                'last_name': 'DEMO',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        staff = response.context['staffs'].first()
        self.assertEqual(staff.id, 4)
        self.assertEqual(staff.last_name, 'DEMO')

    def test_get_all_staff_list_view(self):
        url = reverse('company_all_staff_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
