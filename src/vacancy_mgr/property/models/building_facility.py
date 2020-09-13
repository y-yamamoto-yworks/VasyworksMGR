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
from .building_picture import BuildingPicture
from users.models import User
from enums.models import Facility


class BuildingFacility(models.Model):
    """
    建物周辺施設
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    building = models.ForeignKey(
        Building,
        db_column='building_id',
        related_name='building_facilities',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    facility = models.ForeignKey(
        Facility,
        db_column='facility_id',
        related_name='building_facilities',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    facility_name = models.CharField(_('facility_name'), db_column='facility_name', max_length=100, null=True, blank=True)
    distance = models.IntegerField(_('distance'), db_column='distance', default=0)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    building_picture = models.ForeignKey(
        BuildingPicture,
        db_column='building_picture_id',
        related_name='building_facilities',
        on_delete=models.PROTECT,
        default=0,
    )

    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user = models.ForeignKey(
        User,
        db_column='created_user_id',
        related_name='created_building_facilities',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user = models.ForeignKey(
        User,
        db_column='updated_user_id',
        related_name='updated_building_facilities',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'building_facility'
        ordering = ['priority', 'id']
        verbose_name = _('building_facility')
        verbose_name_plural = _('building_facilities')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)
