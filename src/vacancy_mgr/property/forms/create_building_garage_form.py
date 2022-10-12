"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from enums.models import GarageStatus


class CreateBuildingGarageForm(forms.Form):
    """
    建物ガレージ作成フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['garage_name'] = forms.CharField(
            label=_('駐車場名'),
            max_length=100,
            required=True,
        )

        self.fields['garage_status'] = forms.ModelChoiceField(
            label=_('空き状況'),
            queryset=GarageStatus.objects.filter(
                is_stopped=False,
            ).order_by('priority').all(),
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
