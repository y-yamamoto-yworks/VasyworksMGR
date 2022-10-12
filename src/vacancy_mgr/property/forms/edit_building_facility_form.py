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
from property.models import Building, BuildingFacility


class EditBuildingFacilityForm(forms.ModelForm):
    """
    建物周辺施設フォーム
    """
    class Meta:
        model = BuildingFacility
        fields = [
            'facility_name',
            'distance',
            'priority',
        ]
        labels = {
            'facility_name': _('周辺施設名'),
            'distance': _('距離'),
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
