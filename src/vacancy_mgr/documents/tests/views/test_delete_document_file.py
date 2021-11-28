"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.test import Client
from django.urls import reverse
from django.db import transaction
import warnings


class DeleteDocumentFileViewTest(TestCase):
    """
    書類ファイル削除ビューのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        if transaction.get_autocommit():
            transaction.set_autocommit(False)

        response = self.client.post(
            reverse('login'),
            {'username': 't-kanri', 'password': 'guest1234', },
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        transaction.rollback()

    def test_get_delete_document_file_view(self):
        url = reverse(
            'documents_delete_document_file',
            args=['MQ'],        # 書類サンプル1
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        file = response.context['data']
        self.assertEqual(file.file_title, '書類サンプル1')

    def test_post_delete_document_file_view(self):
        url = reverse(
            'documents_delete_document_file',
            args=['MQ'],        # 書類サンプル1
        )

        response = self.client.post(
            url,
            {
                'confirm': 'on',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '削除しました。')
