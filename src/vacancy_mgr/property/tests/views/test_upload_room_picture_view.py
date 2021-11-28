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


class UploadRoomPictureViewTest(TestCase):
    """
    部屋画像アップロードビューのテスト
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

    def test_get_upload_room_picture_view(self):
        url = reverse(
            'property_upload_room_picture',
            args=['d42f9ba08e1b4fd185c6479ba452af68'],     # リストサンプルマンション1 101号室
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        room = response.context['room']
        self.assertEqual(room.building.building_name, 'リストサンプルマンション1')
        self.assertEqual(room.room_no, '101')

    def test_post_upload_room_picture_view(self):
        oid = 'd42f9ba08e1b4fd185c6479ba452af68'     # リストサンプルマンション1 101号室
        url = reverse(
            'property_upload_room_picture',
            args=[oid],
        )
        url += '?back_url=/property/room/{0}%3Fpage=pictures_page'.format(oid)

        file_name = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_picture.jpg')
        upload_file = SimpleUploadedFile(
            'sample_picture.jpg',
            open(file_name, 'rb').read(),
            'image/jpeg')

        response = self.client.post(
            url,
            {
                'picture_type': '2010',
                'image': upload_file,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '追加しました。')
        room = response.context['room']
        delete_dir = os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', room.building.file_oid)
        shutil.rmtree(delete_dir)
