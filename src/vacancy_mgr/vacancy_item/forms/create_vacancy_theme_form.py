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


class CreateVacancyThemeForm(forms.Form):
    """
    空室情報テーマ作成フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(
            label=_('テーマ名'),
            max_length=50,
            initial='',
            required=True,
        )

        self.fields['title'] = forms.CharField(
            label=_('タイトル'),
            max_length=100,
            initial='',
            required=True,
        )

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
