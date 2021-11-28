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


class DocumentFileListViewTest(TestCase):
    """
    書類ファイル一覧ビューのテスト
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

    def test_get_document_file_list_view(self):
        url = reverse('documents_index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        document_file = response.context['document_files'].first()
        self.assertEqual(document_file.file_title, '書類サンプル1')
