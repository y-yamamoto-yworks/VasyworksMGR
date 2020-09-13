"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import uuid
import urllib.parse
import shutil
import qrcode
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from lib.convert import *
from lib.functions import *
from lib.image_helper import ImageHelper
from property.models import Building, Room


class MediaHelper:
    """ メディアヘルパークラス"""
    @staticmethod
    def upload_binary_file(source_file, destination_file_path):
        """バイナリファイルのアップロード"""
        file_dir = os.path.dirname(destination_file_path)
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)

        with open(destination_file_path, 'wb') as f:
            for chunk in source_file.chunks():
                f.write(chunk)

    @staticmethod
    def get_uuid_filename(filename):
        ext = filename.split('.')[-1]
        ans = "%s.%s" % (uuid.uuid4(), ext)
        ans = ans.replace('-', '')
        return ans

    """
    書類ファイル
    """
    @staticmethod
    def get_document_root():
        """書類ファイルのルートディレクトリ"""
        return os.path.join(settings.MEDIA_ROOT, 'public', 'documents')

    @staticmethod
    def get_upload_document_path(file_name: str):
        """書類ファイルのアップロードパス"""
        if file_name:
            return os.path.join(MediaHelper.get_document_root(),
                                'files',
                                file_name)
        else:
            raise ValueError

    """
    物件別メディアファイル
    """
    @staticmethod
    def get_property_media_root():
        """物件のメディアファイルのルートディレクトリ"""
        return os.path.join(settings.MEDIA_ROOT, 'public', 'buildings')

    @staticmethod
    def get_upload_picture_path(instance: Building, file_name: str):
        """画像のアップロードパス"""
        if instance and file_name:
            return os.path.join(MediaHelper.get_property_media_root(),
                                instance.file_oid,
                                'pictures',
                                file_name)
        else:
            raise ValueError

    @staticmethod
    def get_picture_thumbnail_path(file_path: str):
        """サムネイル画像用のパス"""
        ans = os.path.join(file_path.replace('pictures', 'thumbnails'))

        thumbnail_dir = os.path.dirname(ans)
        if not os.path.isdir(thumbnail_dir):
            os.mkdir(thumbnail_dir)

        return ans

    @staticmethod
    def get_upload_panorama_path(instance: Building, file_name: str):
        """パノラマのアップロードパス"""
        if instance and file_name:
            return os.path.join(MediaHelper.get_property_media_root(),
                                instance.file_oid,
                                'panoramas',
                                file_name)
        else:
            raise ValueError

    @staticmethod
    def get_upload_movie_path(instance: Building, file_name: str):
        """動画のアップロードパス"""
        if instance and file_name:
            return os.path.join(MediaHelper.get_property_media_root(),
                                instance.file_oid,
                                'movies',
                                file_name)
        else:
            raise ValueError

    @staticmethod
    def get_upload_file_path(instance: Building, file_name: str):
        """物件資料ファイルのアップロードパス"""
        if instance and file_name:
            return os.path.join(MediaHelper.get_property_media_root(),
                                instance.file_oid,
                                'files',
                                file_name)
        else:
            raise ValueError
