"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _


class CreateRoomForm(forms.Form):
    """
    部屋作成フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['room_no'] = forms.CharField(
            label=_('部屋番号'),
            max_length=20,
            required=True,
        )

        self.fields['room_floor'] = forms.IntegerField(
            label=_('部屋階数'),
            required=True,
        )

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
