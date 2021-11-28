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


class ManagementInfoListViewTest(TestCase):
    """
    管理お知らせ一覧ビューのテスト
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

    def test_get_management_info_list_view(self):
        url = reverse('info_management_info_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        info = response.context['infos'].first()
        self.assertEqual(info.id, 3)
        self.assertEqual(info.information, '管理お知らせDEMOデータ3')
