"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from company.models import Department


class DepartmentForm(forms.ModelForm):
    """
    部署フォーム
    """
    class Meta:
        model = Department
        fields = [
            'department_name',
            'priority',
            'is_publish_vacancy',
            'postal_code',
            'address',
            'tel',
            'fax',
            'mail',
            'note',
            'is_stopped',
            'is_deleted',
        ]
        labels = {
            'department_name': _('部署名'),
            'priority': _('表示順'),
            'is_publish_vacancy': _('空室情報公開'),
            'postal_code': _('郵便番号'),
            'address': _('住所'),
            'tel': _('電話番号'),
            'fax': _('FAX番号'),
            'mail': _('E-MAIL'),
            'note': _('備考'),
            'is_stopped': _('停止'),
            'is_deleted': _('削除'),
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
