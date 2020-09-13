"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from users.models import User


class UserForm(auth_forms.UserChangeForm):
    """
    ユーザフォーム
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
        self.fields['first_name'].widget.attrs['required'] = True
        self.fields['last_name'].widget.attrs['required'] = True

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'last_name',
            'first_name',
            'email',
            'is_active',
            'is_company_admin',
            'staff',
        ]
        labels = {
            'username': 'ユーザー名',
            'password': 'パスワード',
            'last_name': '姓',
            'first_name': '名',
            'email': 'Eメール',
            'is_active': '有効',
            'is_company_admin': '管理者',
            'staff': 'スタッフ',
        }
