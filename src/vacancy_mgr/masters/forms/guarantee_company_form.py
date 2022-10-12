"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from masters.models import GuaranteeCompany


class GuaranteeCompanyForm(forms.ModelForm):
    """
    保証会社フォーム
    """
    class Meta:
        model = GuaranteeCompany
        fields = [
            'name',
            'priority',
            'is_stopped',
        ]
        labels = {
            'name': _('保証会社名'),
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
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
