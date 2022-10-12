"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from vacancy_item.models import VacancyTheme


class CreateRoomVacancyThemeForm(forms.Form):
    """
    部屋空室テーマ作成フォーム
    """
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        if not user:
            raise ValueError

        super().__init__(*args, **kwargs)

        self.fields['vacancy_theme'] = forms.ModelChoiceField(
            label=_('空室テーマ'),
            queryset=VacancyTheme.objects.filter(is_stopped=False).order_by('priority').all(),
            required=True,
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
