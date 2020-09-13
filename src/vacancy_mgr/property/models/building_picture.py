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
from users.models import User
from enums.models import PictureType

class BuildingPicture(models.Model):
    """
    建物画像
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    building = models.ForeignKey(
        Building,
        db_column='building_id',
        related_name='building_pictures',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    file_name = models.CharField(_('file_name'), db_column='file_name', max_length=255)
    cache_name_thumb = models.CharField(_('cache_name_thumb'), db_column='cache_name_thumb', max_length=255)
    cache_name_s = models.CharField(_('cache_name_s'), db_column='cache_name_s', max_length=255)
    cache_name_m = models.CharField(_('cache_name_m'), db_column='cache_name_m', max_length=255)
    cache_name_l = models.CharField(_('cache_name_l'), db_column='cache_name_l', max_length=255)
    cache_name_org = models.CharField(_('cache_name_org'), db_column='cache_name_org', max_length=255)
    picture_type = models.ForeignKey(
        PictureType,
        db_column='picture_type_id',
        related_name='building_pictures',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_publish_web = models.BooleanField(_('is_publish_web'), db_column='is_publish_web', db_index=True, default=True)
    is_publish_vacancy = models.BooleanField(_('is_publish_vacancy'), db_column='is_publish_vacancy', db_index=True, default=True)
    comment = models.CharField(_('comment'), db_column='comment', max_length=50, null=True, blank=True)
    note = models.CharField(_('note'), db_column='note', max_length=255, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)

    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user = models.ForeignKey(
        User,
        db_column='created_user_id',
        related_name='created_building_pictures',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user = models.ForeignKey(
        User,
        db_column='updated_user_id',
        related_name='updated_building_pictures',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'building_picture'
        ordering = ['priority', 'id']
        verbose_name = _('building_picture')
        verbose_name_plural = _('building_pictures')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)
