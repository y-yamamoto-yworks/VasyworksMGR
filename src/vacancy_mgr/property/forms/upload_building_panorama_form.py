"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from enums.models import PanoramaType


class UploadBuildingPanoramaForm(forms.Form):
    """
    建物パノラマアップロードフォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['panorama_type'] = forms.ModelChoiceField(
            label=_('パノラマ種別'),
            queryset=PanoramaType.objects.filter(
                is_building=True,
                is_stopped=False,
            ).order_by('priority').all(),
            required=True,
        )

        self.fields['panorama'] = forms.FileField(
            label=_('パノラマファイル'),
            required=True,
        )

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
