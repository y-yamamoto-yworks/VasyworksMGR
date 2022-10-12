"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from enums.models import Equipment, EquipmentCategory


class CreateRoomEquipmentForm(forms.Form):
    """
    部屋設備作成フォーム
    """
    def __init__(self, category=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['equipment_category'] = forms.ModelChoiceField(
            label=_('設備カテゴリ'),
            queryset=EquipmentCategory.objects.filter(
                is_stopped=False,
            ).order_by('priority').all(),
            required=False,
        )

        self.fields['equipments'] = forms.ModelMultipleChoiceField(
            label=_('設備'),
            queryset=Equipment.objects.filter(
                is_stopped=False,
            ).order_by('priority').all(),
            widget=forms.SelectMultiple(),
            required=False,
        )
        if category:
            self.fields['equipment_category'].initial = category
            self.fields['equipments'].queryset = Equipment.objects.filter(
                category=category,
                is_stopped=False,
            ).order_by('priority').all()

        self.fields['is_remained'] = forms.BooleanField(
            label=_('残置物'),
            widget=forms.CheckboxInput,
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
