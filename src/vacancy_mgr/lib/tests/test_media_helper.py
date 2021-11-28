"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
import warnings
import os
from lib.media_helper import MediaHelper
from property.models import Building


class MediaHelperTest(TestCase):
    """
    メディアヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_upload_binary_file(self):
        file_path = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_document.pdf')
        upload_file = SimpleUploadedFile(
            'sample_document.pdf',
            open(file_path, 'rb').read(),
            'application/pdf')

        upload_path = os.path.join(settings.MEDIA_ROOT, 'test_data', 'upload_binary_test.pdf')

        MediaHelper.upload_binary_file(upload_file, upload_path)

        self.assertTrue(os.path.exists(upload_path))
        os.remove(upload_path)

    def test_get_uuid_filename(self):
        self.assertRegex(MediaHelper.get_uuid_filename('sample.jpg'), '\.jpg$')
        self.assertRegex(MediaHelper.get_uuid_filename('sample.pdf'), '\.pdf$')

    def test_get_document_root(self):
        self.assertEqual(
            MediaHelper.get_document_root(),
            os.path.join(settings.MEDIA_ROOT, 'public', 'documents'),
        )

    def test_get_upload_document_path(self):
        file_name = 'sample.pdf'
        self.assertEqual(
            MediaHelper.get_upload_document_path(file_name),
            os.path.join(settings.MEDIA_ROOT, 'public', 'documents', 'files', file_name),
        )

    def test_get_property_media_root(self):
        self.assertEqual(
            MediaHelper.get_property_media_root(),
            os.path.join(settings.MEDIA_ROOT, 'public', 'buildings'),
        )

    def test_get_upload_picture_path(self):
        building = Building.objects.get(pk=1)
        file_name = 'sample_picture.jpg'
        self.assertEqual(
            MediaHelper.get_upload_picture_path(building, file_name),
            os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', building.file_oid, 'pictures', file_name),
        )

    def test_get_picture_thumbnail_path(self):
        building = Building.objects.get(pk=1)
        file_name = 'sample_picture.jpg'
        file_path = os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', building.file_oid, 'pictures', file_name)
        self.assertEqual(
            MediaHelper.get_picture_thumbnail_path(file_path),
            os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', building.file_oid, 'thumbnails', file_name),
        )

    def test_get_upload_panorama_path(self):
        building = Building.objects.get(pk=1)
        file_name = 'sample_picture.jpg'
        self.assertEqual(
            MediaHelper.get_upload_panorama_path(building, file_name),
            os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', building.file_oid, 'panoramas', file_name),
        )

    def test_get_upload_movie_path(self):
        building = Building.objects.get(pk=1)
        file_name = 'sample_movie.jpg'
        self.assertEqual(
            MediaHelper.get_upload_movie_path(building, file_name),
            os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', building.file_oid, 'movies', file_name),
        )

    def test_get_upload_file_path(self):
        building = Building.objects.get(pk=1)
        file_name = 'sample_picture.pdf'
        self.assertEqual(
            MediaHelper.get_upload_file_path(building, file_name),
            os.path.join(settings.MEDIA_ROOT, 'public', 'buildings', building.file_oid, 'files', file_name),
        )
