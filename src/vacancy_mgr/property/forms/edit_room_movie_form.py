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
from enums.models import MovieType
from property.models import Room, RoomMovie


class EditRoomMovieForm(forms.ModelForm):
    """
    部屋動画フォーム
    """
    class Meta:
        model = RoomMovie
        fields = [
            'movie_type',
            'comment',
            'note',
            'priority',
            'is_publish_web',
            'is_publish_vacancy',
        ]
        labels = {
            'movie_type': _('動画種別'),
            'priority': _('優先順'),
            'comment': _('コメント'),
            'note': _('備考'),
            'is_publish_vacancy': _(''),
            'is_publish_web': _(''),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['movie_type'].queryset = MovieType.objects.filter(
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
