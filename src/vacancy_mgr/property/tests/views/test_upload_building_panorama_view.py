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
import shutil


class UploadBuildingPanoramaViewTest(TestCase):
    """
    建物パノラマアップロードビューのテスト
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

    def test_get_upload_building_panorama_view(self):
        url = reverse(
            'property_upload_building_panorama',
            args=['bf541cee9a9144338467277f3fc24717'],     # リストサンプルマンション1
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        building = response.context['building']
        self.assertEqual(building.building_name, 'リストサンプルマンション1')

    def test_post_upload_building_panorama_view(self):
        oid = 'bf541cee9a9144338467277f3fc24717'     # リストサンプルマンション1
        url = reverse(
            'property_upload_building_panorama',
            args=[oid],
        )
        url += '?back_url=/property/building/{0}%3Fpage=pictures_page%23panorama-anchor'.format(oid)

        file_name = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_panorama.jpg')
        upload_file = SimpleUploadedFile(
            'sample_panorama.jpg',
            open(file_name, 'rb').read(),
            'image/jpeg')

        response = self.client.post(
            url,
            {
                'panorama_type': '1010',
                'panorama': upload_file,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '追加しました。')
        building = response.context['building']
        delete_dir = os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', building.file_oid)
        shutil.rmtree(delete_dir)
