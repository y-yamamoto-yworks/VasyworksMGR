"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from property.models import Room


class SelectOtherRoomForm(forms.Form):
    """
    同一建物内の他の部屋の選択フォーム
    """
    def __init__(self, *args, **kwargs):
        room = kwargs.pop('room')
        if not room:
            raise ValueError("部屋の指定が不正です。")

        super().__init__(*args, **kwargs)

        self.fields['selected_room'] = forms.ModelChoiceField(
            label=_('部屋'),
            queryset=room.other_rooms,
            required=True,
        )
        self.fields['selected_room'].widget.attrs['v-model'] = 'selectedRoom'
        self.fields['selected_room'].widget.attrs['v-on:change'] = 'changeSelectedRoom($event)'

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
