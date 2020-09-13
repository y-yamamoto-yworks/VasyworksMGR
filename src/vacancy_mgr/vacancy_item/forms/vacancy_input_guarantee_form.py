"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from vacancy_item.models import VacancyInputGuarantee


class VacancyInputGuaranteeForm(forms.ModelForm):
    """
    空室入力保証会社フォーム
    """
    class Meta:
        model = VacancyInputGuarantee
        fields = [
            'input_contents',
            'priority',
            'is_stopped',
        ]
        labels = {
            'input_contents': _('入力内容'),
            'priority': _('表示順'),
            'is_stopped': _('停止'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
