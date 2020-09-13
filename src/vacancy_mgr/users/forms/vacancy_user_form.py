"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from users.models import VacancyUser


class VacancyUserForm(auth_forms.UserChangeForm):
    """
    空室情報閲覧ユーザフォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                if field != self.fields['password']:
                    field.widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['required'] = True
        self.fields['display_name'].widget.attrs['required'] = True

    class Meta:
        model = VacancyUser
        fields = [
            'username',
            'password',
            'display_name',
            'email',
            'is_active',
            'is_company',
            'level',
            'allow_org_image',
            'trader_name',
            'trader_department_name',
            'trader_department_tel',
            'trader_department_address',
            'note',
        ]
        labels = {
            'username': 'ユーザー名',
            'password': 'パスワード',
            'display_name': '表示名',
            'email': 'Eメール',
            'is_active': '有効',
            'is_company': '自社',
            'level': '閲覧レベル',
            'allow_org_image': 'オリジナル画像参照',
            'trader_name': '業者名',
            'trader_department_name': '部署名',
            'trader_department_tel': '部署電話番号',
            'trader_department_address': '部署住所',
            'note': '備考',
        }
