"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from enums.models import MovieType


class UploadRoomMovieForm(forms.Form):
    """
    部屋動画アップロードフォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['movie_type'] = forms.ModelChoiceField(
            label=_('動画種別'),
            queryset=MovieType.objects.filter(
                is_room=True,
                is_stopped=False,
            ).order_by('priority').all(),
            required=True,
        )

        self.fields['movie'] = forms.FileField(
            label=_('動画ファイル'),
            required=True,
            widget=forms.FileInput(attrs={'accept': 'video/*'}),
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
