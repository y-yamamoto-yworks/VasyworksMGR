"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import re
from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from enums.models import GarageStatus
from property.models import Building, BuildingGarage


class EditBuildingGarageForm(forms.ModelForm):
    """
    建物周辺施設フォーム
    """
    class Meta:
        model = BuildingGarage
        fields = [
            'garage_name',
            'garage_status',
            'priority',
            'garage_fee',
            'garage_fee_tax_type',
            'garage_charge',
            'garage_charge_tax_type',
            'garage_deposit',
            'garage_deposit_tax_type',
            'certification_fee',
            'certification_fee_tax_type',
            'initial_cost_name1',
            'initial_cost1',
            'initial_cost_tax_type1',
            'initial_cost_name2',
            'initial_cost2',
            'initial_cost_tax_type2',
            'initial_cost_name3',
            'initial_cost3',
            'initial_cost_tax_type3',
            'allow_no_room',
            'width',
            'length',
            'height',
            'comment',
            'note',
        ]
        labels = {
            'garage_name': _('駐車場名'),
            'garage_status': _('空き状況'),
            'priority': _('優先順'),
            'garage_fee': _('月額'),
            'garage_fee_tax_type': _('月額税種別'),
            'garage_charge': _('手数料'),
            'garage_charge_tax_type': _('手数料税種別'),
            'garage_deposit': _('保証料'),
            'garage_deposit_tax_type': _('保証料税種別'),
            'certification_fee': _('車庫証明費用'),
            'certification_fee_tax_type': _('車庫証明費用税種別'),
            'initial_cost_name1': _('初期費用名1'),
            'initial_cost1': _('初期費用1'),
            'initial_cost_tax_type1': _('初期費用税種別1'),
            'initial_cost_name2': _('初期費用名2'),
            'initial_cost2': _('初期費用2'),
            'initial_cost_tax_type2': _('初期費用税種別2'),
            'initial_cost_name3': _('初期費用名3'),
            'initial_cost3': _('初期費用3'),
            'initial_cost_tax_type3': _('初期費用税種別3'),
            'allow_no_room': _('外部貸し可'),
            'width': _('幅'),
            'length': _('奥行き'),
            'height': _('高さ'),
            'comment': _('コメント'),
            'note': _('備考'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['note'].widget = forms.Textarea()

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
