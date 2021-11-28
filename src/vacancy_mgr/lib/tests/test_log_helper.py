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
from lib.log_helper import LogHelper
from enums.models import RoomStatus
from users.models import User
from property.models import Room, RoomStatusLog


class LogHelperTest(TestCase):
    """
    ログヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_write_room_status_log(self):
        user = User.objects.get(pk=1)
        room = Room.objects.get(pk=1)
        status = RoomStatus.objects.get(pk=2)
        last_status = RoomStatus.objects.get(pk=1)
        LogHelper.write_room_status_log(user, room, status, last_status)
        log = RoomStatusLog.objects.filter(
            created_user=user,
            room=room,
            room_status=status,
            last_room_status=last_status,
        ).all()
        self.assertEqual(log.count(), 1)
