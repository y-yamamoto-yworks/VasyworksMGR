"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
import warnings
import os
from PIL import Image
from lib.image_helper import ImageHelper


class ImageHelperTest(TestCase):
    """
    画像ヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_save_image(self):
        image_file = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_picture.jpg')
        image = Image.open(image_file)
        save_path = os.path.join(settings.MEDIA_ROOT, 'test_data', 'save_image_test.jpg')
        ImageHelper.save_image(image, save_path)
        self.assertTrue(os.path.exists(save_path))
        os.remove(save_path)

    def test_save_and_rotate_image(self):
        image_file = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_rotate_picture.jpg')
        image = Image.open(image_file)
        save_path = os.path.join(settings.MEDIA_ROOT, 'test_data', 'save_rotate_image_test.jpg')
        ImageHelper.save_image(image, save_path)
        self.assertTrue(os.path.exists(save_path))
        os.remove(save_path)

    def test_copy_and_delete_image_file(self):
        src = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_picture.jpg')
        dest = os.path.join(settings.MEDIA_ROOT, 'test_data', 'copy_image_test.jpg')
        ImageHelper.copy_image_file(src, dest)
        self.assertTrue(os.path.exists(dest))
        ImageHelper.delete_image(dest)
        self.assertFalse(os.path.exists(dest))

    def test_make_qrcode(self):
        dest = os.path.join(settings.MEDIA_ROOT, 'test_data', 'qrcode_test.jpg')
        ImageHelper.make_qrcode('QR Code Test', dest)
        self.assertTrue(os.path.exists(dest))
        os.remove(dest)
        self.assertFalse(os.path.exists(dest))
