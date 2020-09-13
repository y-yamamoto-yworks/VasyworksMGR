"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect, render, get_object_or_404


class CreateWithNameForm(forms.Form):
    """
    オブジェクト作成フォーム（名称）
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(
            label=_('名称'),
            max_length=255,
            initial='',
            required=True,
        )
        self.fields['name'].widget.attrs['@keydown.enter'] = 'trigger'
        self.fields['kana'] = forms.CharField(
            label=_('名称カナ'),
            max_length=255,
            initial='',
            required=True,
        )
        self.fields['kana'].widget.attrs['@keydown.enter'] = 'trigger'

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
