"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from company.models import Company


class CompanyForm(forms.ModelForm):
    """
    会社フォーム
    """
    class Meta:
        model = Company
        fields = [
            'company_name',
            'company_kana',
            'shop_name',
            'api_key',
            'internal_api_key',
            'postal_code',
            'address',
            'tel',
            'fax',
            'mail',
            'agency_no',
            'pm_no',
            'water_mark',
        ]
        labels = {
            'company_name': _('会社名'),
            'company_kana': _('会社名カナ'),
            'shop_name': _('店舗名'),
            'api_key': _('APIキー'),
            'internal_api_key': _('内部APIキー'),
            'postal_code': _('郵便番号'),
            'address': _('住所'),
            'tel': _('電話番号'),
            'fax': _('FAX番号'),
            'mail': _('E-MAIL'),
            'agency_no': _('宅建免許番号'),
            'pm_no': _('管理登録番号'),
            'water_mark': _('透かし文字'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['api_key'].widget = forms.HiddenInput()
        self.fields['api_key'].widget.attrs['v-model'] = 'apiKey'
        self.fields['internal_api_key'].widget = forms.HiddenInput()
        self.fields['internal_api_key'].widget.attrs['v-model'] = 'internalApiKey'

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
