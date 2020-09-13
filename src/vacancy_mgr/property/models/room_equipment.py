"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *
from .building import Building
from .room import Room
from users.models import User
from enums.models import Equipment


class  RoomEquipment(models.Model):
    """
    部屋設備
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    building = models.ForeignKey(
        Building,
        db_column='building_id',
        related_name='room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    room = models.ForeignKey(
        Room,
        db_column='room_id',
        related_name='room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    equipment = models.ForeignKey(
        Equipment,
        db_column='equipment_id',
        related_name='room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_remained = models.BooleanField(_('is_remained'), db_column='is_remained', default=False)
    note = models.TextField(_('note'), db_column='note', max_length=2000, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)

    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user = models.ForeignKey(
        User,
        db_column='created_user_id',
        related_name='created_room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user = models.ForeignKey(
        User,
        db_column='updated_user_id',
        related_name='updated_room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'room_equipment'
        ordering = ['priority', 'id']
        verbose_name = _('room_equipment')
        verbose_name_plural = _('room_equipments')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)
