"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from enums.models import LandmarkType
from masters.models import Landmark


class CreateBuildingLandmarkForm(forms.Form):
    """
    建物ランドマーク作成フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['landmark_type'] = forms.ModelChoiceField(
            label=_('ランドマーク種別'),
            queryset=LandmarkType.objects.filter(
                is_stopped=False,
            ).order_by('priority').all(),
            required=False,
        )
        self.fields['landmark_type'].widget.attrs['v-model'] = 'landmarkType'
        self.fields['landmark_type'].widget.attrs['v-on:change'] = 'changeLandmarkType($event)'

        self.fields['landmark'] = forms.ModelChoiceField(
            label=_('ランドマーク'),
            queryset=Landmark.objects.filter(
                is_stopped=False,
            ).order_by('priority').all(),
            required=True,
        )
        self.fields['landmark'].widget.attrs['v-model'] = 'landmark'


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
