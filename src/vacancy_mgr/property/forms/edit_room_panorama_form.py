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
from enums.models import PanoramaType
from property.models import Room, RoomPanorama


class EditRoomPanoramaForm(forms.ModelForm):
    """
    部屋パノラマフォーム
    """
    class Meta:
        model = RoomPanorama
        fields = [
            'panorama_type',
            'comment',
            'note',
            'priority',
            'is_publish_web',
            'is_publish_vacancy',
        ]
        labels = {
            'panorama_type': _('パノラマ種別'),
            'priority': _('優先順'),
            'comment': _('コメント'),
            'note': _('備考'),
            'is_publish_vacancy': _(''),
            'is_publish_web': _(''),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['panorama_type'].queryset = PanoramaType.objects.filter(
            is_room=True,
            is_stopped=False,
        ).order_by('priority').all()

        self.fields['note'].widget = forms.Textarea()

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
