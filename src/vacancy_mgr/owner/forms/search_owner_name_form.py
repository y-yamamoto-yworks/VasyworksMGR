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


class SearchOwnerNameForm(forms.Form):
    """
    オーナー名称検索フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner_name'] = forms.CharField(
            label=_('オーナー名'),
            required=False,
        )
        self.fields['owner_name'].widget.attrs['v-model'] = 'owner_name'

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
