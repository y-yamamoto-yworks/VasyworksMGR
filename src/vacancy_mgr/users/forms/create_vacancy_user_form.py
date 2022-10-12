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


class CreateVacancyUserForm(auth_forms.UserCreationForm):
    """
    空室情報閲覧ユーザ作成フォーム
    """
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

    class Meta:
        model = VacancyUser
        fields = [
            'username',
            'password1',
            'password2',
            ]
