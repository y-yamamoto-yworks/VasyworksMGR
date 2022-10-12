"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import re
from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from property.models import Room, RoomEquipment


class EditRoomEquipmentForm(forms.ModelForm):
    """
    部屋設備フォーム
    """
    class Meta:
        model = RoomEquipment
        fields = [
            'is_remained',
            'note',
            'priority',
        ]
        labels = {
            'is_remained': _('残置物'),
            'note': _('備考'),
            'priority': _('優先順'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
