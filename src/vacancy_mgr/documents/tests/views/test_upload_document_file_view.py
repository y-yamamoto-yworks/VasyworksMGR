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
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
import warnings
import os
import datetime
from documents.models import DocumentFile


class UploadDocumentFileViewTest(TestCase):
    """
    書類ファイルアップロードビューのテスト
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

    def test_get_upload_building_file_view(self):
        url = reverse('documents_upload_document_file')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_post_upload_document_file_view(self):
        url = reverse('documents_upload_document_file')

        file_name = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_document.pdf')
        upload_file = SimpleUploadedFile(
            'sample_document.pdf',
            open(file_name, 'rb').read(),
            'application/pdf')

        file_title = '建物ファイルアップロードテスト' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        response = self.client.post(
            url,
            {
                'file_title': file_title,
                'file': upload_file,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '追加しました。')
        document_file = DocumentFile.objects.filter(file_title=file_title).first()
        file_path = os.path.join(settings.MEDIA_ROOT, 'public', 'documents', 'files', document_file.file_name)
        os.remove(file_path)
