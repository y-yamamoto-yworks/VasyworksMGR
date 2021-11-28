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


class OwnerListViewTest(TestCase):
    """
    オーナー一覧ビューのテスト
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

    def test_get_owner_list_view(self):
        url = reverse('owner_owner_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        owner = response.context['owners'].first()
        self.assertEqual(owner.id, 3)
        self.assertEqual(owner.owner_name, '一条　剣之介')

    def test_post_owner_list_view(self):
        url = reverse('owner_owner_list')
        response = self.client.post(
            url,
            {
                'owner_name': 'DEMO',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        owner = response.context['owners'].first()
        self.assertEqual(owner.id, 2)
        self.assertEqual(owner.owner_name, 'DEMOオーナー')

    def test_get_all_owner_list_view(self):
        url = reverse('owner_all_owner_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
