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
from enums.models import PictureType
from property.models import Building, BuildingPicture


class EditBuildingPictureForm(forms.ModelForm):
    """
    建物画像フォーム
    """
    class Meta:
        model = BuildingPicture
        fields = [
            'picture_type',
            'comment',
            'note',
            'priority',
            'is_publish_web',
            'is_publish_vacancy',
        ]
        labels = {
            'picture_type': _('画像種別'),
            'priority': _('優先順'),
            'comment': _('コメント'),
            'note': _('備考'),
            'is_publish_vacancy': _(''),
            'is_publish_web': _(''),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['picture_type'].queryset = PictureType.objects.filter(
            is_building=True,
            is_stopped=False,
        ).order_by('priority').all()

        self.fields['note'].widget = forms.Textarea()

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
