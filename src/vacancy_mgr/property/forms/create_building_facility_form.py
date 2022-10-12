"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from enums.models import Facility


class CreateBuildingFacilityForm(forms.Form):
    """
    建物周辺施設作成フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['facility'] = forms.ModelChoiceField(
            label=_('周辺施設'),
            queryset=Facility.objects.filter(
                is_stopped=False,
            ).order_by('priority').all(),
            required=True,
        )

        self.fields['facility_name'] = forms.CharField(
            label=_('施設名'),
            max_length=100,
            required=False,
        )

        self.fields['distance'] = forms.IntegerField(
            label=_('距離'),
            required=False,
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
