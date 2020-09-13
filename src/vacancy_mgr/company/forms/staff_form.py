"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from company.models import Staff


class StaffForm(forms.ModelForm):
    """
    スタッフフォーム
    """
    class Meta:
        model = Staff
        fields = [
            'last_name',
            'first_name',
            'post_name',
            'vacancy_name',
            'priority',
            'department',
            'tel1',
            'tel2',
            'mail',
            'is_pm_staff',
            'is_publish_vacancy',
            'is_stopped',
            'is_deleted',
        ]
        labels = {
            'last_name': _('姓'),
            'first_name': _('名'),
            'post_name': _('役職'),
            'vacancy_name': _('空室情報名'),
            'priority': _('表示順'),
            'department': _('部署'),
            'tel1': _('電話番号1'),
            'tel2': _('電話番号2'),
            'mail': _('E-MAIL'),
            'is_pm_staff': _('管理スタッフ'),
            'is_publish_vacancy': _('空室情報公開'),
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
            else:
                field.widget.attrs['class'] = 'form-control'
