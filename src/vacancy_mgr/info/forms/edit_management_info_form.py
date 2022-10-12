"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import re
from django import forms
from django.utils.translation import gettext_lazy as _
from info.models import ManagementInfo


class EditManagementInfoForm(forms.ModelForm):
    """
    管理お知らせフォーム
    """
    class Meta:
        model = ManagementInfo
        fields = [
            'information',
            'link_url',
            'start_date',
            'end_date',
            'is_emphasized',
            'priority',
        ]
        labels = {
            'information': _('お知らせ内容'),
            'link_url': _('リンクURL'),
            'start_date': _('公開開始日'),
            'end_date': _('公開終了日'),
            'is_emphasized': _('強調表示'),
            'priority': _('優先順'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['information'].widget = forms.Textarea()
        self.fields['start_date'].widget = forms.DateInput(attrs={"type": "date"}, format=['%Y-%m-%d'])
        self.fields['end_date'].widget = forms.DateInput(attrs={"type": "date"}, format=['%Y-%m-%d'])

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_start_date(self):
        target_date = self.cleaned_data['start_date']
        if target_date:
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', target_date):
                raise forms.ValidationError('日付はyyyy-mm-ddの形式で入力してください。')
        return target_date

    def clean_end_date(self):
        target_date = self.cleaned_data['end_date']
        if target_date:
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', target_date):
                raise forms.ValidationError('日付はyyyy-mm-ddの形式で入力してください。')
        return target_date
