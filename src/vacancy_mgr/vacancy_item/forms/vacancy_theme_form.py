"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from vacancy_item.models import VacancyTheme


class VacancyThemeForm(forms.ModelForm):
    """
    空室情報テーマフォーム
    """
    class Meta:
        model = VacancyTheme
        fields = [
            'name',
            'title',
            'description',
            'priority',
            'room_auth_level',
            'is_publish',
            'is_stopped',
        ]
        labels = {
            'name': _('テーマ名'),
            'title': _('タイトル'),
            'description': _('説明'),
            'priority': _('表示順'),
            'room_auth_level': _('閲覧レベル'),
            'is_publish': _('公開'),
            'is_stopped': _('停止'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
