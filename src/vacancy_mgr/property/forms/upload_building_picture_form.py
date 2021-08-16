"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from enums.models import PictureType


class UploadBuildingPictureForm(forms.Form):
    """
    建物画像アップロードフォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['picture_type'] = forms.ModelChoiceField(
            label=_('画像種別'),
            queryset=PictureType.objects.filter(
                is_building=True,
                is_stopped=False,
            ).order_by('priority').all(),
            required=True,
        )

        self.fields['image'] = forms.ImageField(
            label=_('画像ファイル'),
            required=True,
            widget=forms.FileInput(attrs={'accept': 'image/jpeg, image/png'}),
        )

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
