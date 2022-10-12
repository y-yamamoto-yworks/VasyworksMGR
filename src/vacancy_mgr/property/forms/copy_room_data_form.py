"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from property.models import Room
from company.models import Company


class CopyRoomDataForm(forms.Form):
    """
    同一建物内の他の部屋のデータコピーフォーム
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

        self.fields['base'] = forms.BooleanField(
            label=_('基本情報'),
            initial=True,
            required=False,
        )

        self.fields['vacancy'] = forms.BooleanField(
            label=_('空室掲載'),
            initial=True,
            required=False,
        )

        self.fields['web'] = forms.BooleanField(
            label=_('WEB掲載'),
            initial=True,
            required=False,
        )

        self.fields['layout'] = forms.BooleanField(
            label=_('間取り'),
            initial=True,
            required=False,
        )

        self.fields['monthly_cost'] = forms.BooleanField(
            label=_('月額費用'),
            initial=True,
            required=False,
        )

        self.fields['initial_cost'] = forms.BooleanField(
            label=_('初期費用'),
            initial=True,
            required=False,
        )

        self.fields['renewal_cost'] = forms.BooleanField(
            label=_('更新・再契約'),
            initial=True,
            required=False,
        )

        self.fields['features'] = forms.BooleanField(
            label=_('特徴'),
            initial=True,
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
