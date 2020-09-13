"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *
from users.models import User


class ManagementInfo(models.Model):
    """
    管理お知らせ
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    information = models.CharField(_('information'), db_column='information', max_length=255)
    link_url = models.URLField(_('link_url'), db_column='link_url', null=True, blank=True)
    start_date = models.CharField(_('start_date'), db_column='start_date', db_index=True, max_length=10)
    end_date = models.CharField(_('end_date'), db_column='end_date', db_index=True, max_length=10)
    is_emphasized = models.BooleanField(_('is_emphasized'), db_column='is_emphasized', default=False)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user = models.ForeignKey(
        User,
        db_column='created_user_id',
        related_name='created_management_infos',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user = models.ForeignKey(
        User,
        db_column='updated_user_id',
        related_name='updated_management_infos',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'management_info'
        ordering = ['priority', '-start_date', 'end_date', 'id']
        verbose_name = _('management_info')
        verbose_name_plural = _('management_infos')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)
