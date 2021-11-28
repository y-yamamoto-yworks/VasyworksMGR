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
from lib.room_copy_helper import RoomCopyHelper
from users.models import User
from property.models import Room


class RoomCopyHelperTest(TestCase):
    """
    部屋データコピーヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_copy_room_data(self):
        src = Room.objects.get(pk=3)        # 表示項目確認用マンション DEMO1号室
        dest = Room.objects.get(pk=19)       # 表示項目確認用マンション DEMO4号室
        user = User.objects.get(pk=1)
        RoomCopyHelper.copy_room_data(src, dest, user, all=True)

        self.assertEqual(src.rent_upper, dest.rent_upper)   # 賃料上限

    def test_copy_room_equipments(self):
        src = Room.objects.get(pk=3)        # 表示項目確認用マンション DEMO1号室
        dest = Room.objects.get(pk=19)       # 表示項目確認用マンション DEMO4号室
        user = User.objects.get(pk=1)
        RoomCopyHelper.copy_room_equipments(src, dest, user)

        self.assertEqual(
            src.room_equipments.filter(is_deleted=False).count(),
            dest.room_equipments.filter(is_deleted=False).count(),
        )

    def test_copy_room_pictures(self):
        src_ids = [13, 14]      # 表示項目確認用マンション DEMO1号室 間取図 居室
        dest = Room.objects.get(pk=20)       # 表示項目確認用マンション DEMO5号室
        user = User.objects.get(pk=1)
        RoomCopyHelper.copy_room_pictures(src_ids, dest, user)

        self.assertEqual(dest.room_pictures.all().count(), 2)
