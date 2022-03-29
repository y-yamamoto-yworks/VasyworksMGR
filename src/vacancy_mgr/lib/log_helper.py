"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils import timezone
from .convert import *
from .functions import *
from enums.models import RoomStatus
from users.models import User
from property.models import Room, RoomStatusLog


class LogHelper:
    """ログヘルパークラス"""
    @staticmethod
    def write_room_status_log(user: User, room: Room, status: RoomStatus, last_status: RoomStatus = None):
        """部屋状況ログの書き込み"""
        if settings.DEMO:
            return

        if room and status:
            data = RoomStatusLog()
            data.building = room.building
            data.room = room
            data.room_status = status
            data.last_room_status = last_status

            data.created_at = timezone.now()
            data.created_user = user

            data.save()
