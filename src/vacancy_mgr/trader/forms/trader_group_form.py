"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from trader.models import TraderGroup


class TraderGroupForm(forms.ModelForm):
    """
    賃貸管理業者グループフォーム
    """
    class Meta:
        model = TraderGroup
        fields = [
            'trader_group_name',
            'trader_group_kana',
            'note',
            'is_stopped',
            'is_deleted',
        ]
        labels = {
            'trader_group': _('賃貸管理業者グループ'),
            'trader_name': _('賃貸管理業者名'),
            'trader_kana': _('賃貸管理業者名カナ'),
            'postal_code': _('郵便番号'),
            'address': _('住所'),
            'tel1': _('電話番号1'),
            'tel2': _('電話番号2'),
            'fax': _('FAX番号'),
            'mail': _('E-MAIL'),
            'no_trading': _('取引不可'),
            'no_portal': _('ポータル掲載不可'),
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
