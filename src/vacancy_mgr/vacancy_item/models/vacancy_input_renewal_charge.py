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
from lib.functions import *


class VacancyInputRenewalCharge(models.Model):
    """
    空室入力更新事務手数料
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    input_contents = models.CharField(_('input_contents'), db_column='input_contents', max_length=255)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'vacancy_input_renewal_charge'
        ordering = ['priority', 'id']
        verbose_name = _('vacancy_input_renewal_charge')
        verbose_name_plural = _('vacancy_input_renewal_charges')

    def __str__(self):
        return self.input_contents

    @property
    def idb64(self):
        return base64_decode_id(self.pk)
