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
from masters.models import Railway
from property.models import Building


class EditBuildingForm(forms.ModelForm):
    """
    建物フォーム
    """
    class Meta:
        model = Building
        fields = [
            'building_code',
            'building_name',
            'building_kana',
            'building_old_name',
            'postal_code',
            'pref',
            'city',
            'town_address',
            'town_name',
            'house_no',
            'building_no',
            'area',
            'elementary_school',
            'elementary_school_distance',
            'junior_high_school',
            'junior_high_school_distance',
            'around_note',
            'management_type',
            'department',
            'staff1',
            'staff2',
            'priority_level',
            'agency_department',
            'owner',
            'owner_note',
            'trader',
            'register_address',
            'register_name',
            'register_building_no',
            'register_no',
            'arrival_type1',
            'station1',
            'station_time1',
            'bus_stop1',
            'bus_stop_time1',
            'arrival_type2',
            'station2',
            'station_time2',
            'bus_stop2',
            'bus_stop_time2',
            'arrival_type3',
            'station3',
            'station_time3',
            'bus_stop3',
            'bus_stop_time3',
            'building_type',
            'building_type_comment',
            'structure',
            'structure_comment',
            'building_rooms',
            'building_floors',
            'building_undergrounds',
            'build_year',
            'build_month',
            'bike_parking_type',
            'with_bike_parking_roof',
            'bike_parking_fee_lower',
            'bike_parking_fee_upper',
            'bike_parking_fee_tax_type',
            'bike_parking_note',
            'garage_type',
            'garage_status',
            'garage_distance',
            'garage_fee_lower',
            'garage_fee_upper',
            'garage_fee_tax_type',
            'garage_charge_lower',
            'garage_charge_upper',
            'garage_charge_tax_type',
            'garage_note',
            'building_management_company',
            'building_management_address',
            'building_management_tel',
            'building_management_no',
            'building_management_note',
            'agreement_existence',
            'apartment_manager_comment',
            'auto_lock_no',
            'is_hidden_vacancy',
            'is_vacancy_recommend',
            'vacancy_rent_comment',
            'vacancy_condo_fees_comment',
            'vacancy_water_comment',
            'vacancy_electric_comment',
            'vacancy_gas_comment',
            'vacancy_internet_comment',
            'vacancy_cancel_notice_comment',
            'vacancy_short_cancel_comment',
            'vacancy_payment_comment',
            'vacancy_guarantee_comment',
            'vacancy_insurance_comment',
            'vacancy_guarantor_limit_comment',
            'vacancy_document_price_comment',
            'vacancy_renewal_fee_comment',
            'vacancy_renewal_charge_comment',
            'vacancy_auto_lock_comment',
            'vacancy_security_comment',
            'vacancy_bike_parking_comment',
            'vacancy_garage_comment',
            'vacancy_cleaning_comment',
            'vacancy_change_lock_comment',
            'vacancy_portal_note',
            'vacancy_catch_copy',
            'vacancy_appeal',
            'vacancy_note',
            'is_hidden_web',
            'web_catch_copy',
            'web_appeal',
            'web_note',
            'tenant_note',
            'garbage_note',
            'private_note',
            'management_note',
        ]
        labels = {
            'building_code': _('自社コード'),
            'building_name': _('建物名称'),
            'building_kana': _('建物名称カナ'),
            'building_old_name': _('建物旧名称'),
            'postal_code': _('郵便番号'),
            'pref': _('都道府県'),
            'city': _('市区'),
            'town_address': _('町域'),
            'town_name': _('町名'),
            'house_no': _('番地'),
            'building_no': _('棟番号'),
            'area': _('エリア'),
            'elementary_school': _('小学校区'),
            'elementary_school_distance': _('小学校距離'),
            'junior_high_school': _('中学校区'),
            'junior_high_school_distance': _('中学校距離'),
            'around_note': _('周辺備考'),
            'management_type': _('管理種別'),
            'department': _('管理部署'),
            'staff1': _('担当スタッフ1'),
            'staff2': _('担当スタッフ2'),
            'priority_level': _('優先レベル'),
            'agency_department': _('仲介部署'),
            'owner': _('オーナー'),
            'owner_note': _('オーナー備考'),
            'trader': _('賃貸管理業者'),
            'register_address': _('登記地番'),
            'register_name': _('登記名義人'),
            'register_building_no': _('登記家屋番号'),
            'register_no': _('登記不動産番号'),
            'arrival_type1': _('駅到着種別1'),
            'station1': _('駅1'),
            'station_time1': _('駅到着時間1'),
            'bus_stop1': _('バス停1'),
            'bus_stop_time1': _('バス停到着時間1'),
            'arrival_type2': _('駅到着種別2'),
            'station2': _('駅2'),
            'station_time2': _('駅到着時間2'),
            'bus_stop2': _('バス停2'),
            'bus_stop_time2': _('バス停到着時間2'),
            'arrival_type3': _('駅到着種別3'),
            'station3': _('駅3'),
            'station_time3': _('駅到着時間3'),
            'bus_stop3': _('バス停3'),
            'bus_stop_time3': _('バス停到着時間3'),
            'building_type': _('建物種別'),
            'building_type_comment': _('建物種別コメント'),
            'structure': _('構造'),
            'structure_comment': _('構造コメント'),
            'building_rooms': _('総戸数'),
            'building_floors': _('建物階数'),
            'building_undergrounds': _('建物地下階数'),
            'build_year': _('完成年'),
            'build_month': _('完成月'),
            'bike_parking_type': _('駐輪場種別'),
            'with_bike_parking_roof': _('駐輪場屋根付フラグ'),
            'bike_parking_fee_lower': _('駐輪場月額下限'),
            'bike_parking_fee_upper': _('駐輪場月額上限'),
            'bike_parking_fee_tax_type': _('駐輪場月額税種別'),
            'bike_parking_note': _('駐輪場備考'),
            'garage_type': _('駐車場種別'),
            'garage_status': _('駐車場空き状況'),
            'garage_distance': _('駐車場距離'),
            'garage_fee_lower': _('駐車場月額下限'),
            'garage_fee_upper': _('駐車場月額上限'),
            'garage_fee_tax_type': _('駐車場月額税種別'),
            'garage_charge_lower': _('駐車場手数料下限'),
            'garage_charge_upper': _('駐車場手数料上限'),
            'garage_charge_tax_type': _('駐車場手数料税種別'),
            'garage_note': _('駐車場備考'),
            'building_management_company': _('建物管理会社名'),
            'building_management_address': _('建物管理会社住所'),
            'building_management_tel': _('建物管理会社電話番号'),
            'building_management_no': _('建物管理会社登録番号'),
            'building_management_note': _('建物管理会社備考'),
            'agreement_existence': _('管理規約有無'),
            'apartment_manager_comment': _('管理人コメント'),
            'auto_lock_no': _('オートロック番号'),
            'is_hidden_vacancy': _('空室情報非公開フラグ'),
            'is_vacancy_recommend': _('空室情報おすすめフラグ'),
            'vacancy_rent_comment': _('空室情報賃料コメント'),
            'vacancy_condo_fees_comment': _('空室情報共益費コメント'),
            'vacancy_water_comment': _('空室情報水道コメント'),
            'vacancy_electric_comment': _('空室情報電気コメント'),
            'vacancy_gas_comment': _('空室情報ガスコメント'),
            'vacancy_internet_comment': _('空室情報インターネットコメント'),
            'vacancy_cancel_notice_comment': _('空室情報解約通知コメント'),
            'vacancy_short_cancel_comment': _('空室情報短期解約コメント'),
            'vacancy_payment_comment': _('空室情報賃料支払コメント'),
            'vacancy_guarantee_comment': _('空室情報保証会社コメント'),
            'vacancy_insurance_comment': _('空室情報火災保険コメント'),
            'vacancy_guarantor_limit_comment': _('空室情報保証人極度額コメント'),
            'vacancy_document_price_comment': _('空室情報書類代コメント'),
            'vacancy_renewal_fee_comment': _('空室情報更新料コメント'),
            'vacancy_renewal_charge_comment': _('空室情報更新事務手数料コメント'),
            'vacancy_auto_lock_comment': _('空室情報オートロックコメント'),
            'vacancy_security_comment': _('空室情報防犯コメント'),
            'vacancy_bike_parking_comment': _('空室情報駐輪場コメント'),
            'vacancy_garage_comment': _('空室情報駐輪場コメント'),
            'vacancy_cleaning_comment': _('空室情報退去時清掃コメント'),
            'vacancy_change_lock_comment': _('空室情報鍵交換コメント'),
            'vacancy_portal_note': _('空室情報ポータル掲載備考'),
            'vacancy_catch_copy': _('空室情報キャッチコピー'),
            'vacancy_appeal': _('空室情報アピール'),
            'vacancy_note': _('空室情報備考'),
            'is_hidden_web': _('WEB非公開フラグ'),
            'web_catch_copy': _('WEBサイトキャッチコピー'),
            'web_appeal': _('WEBサイトアピール'),
            'web_note': _('WEBサイト公開備考'),
            'tenant_note': _('テナント関連備考'),
            'garbage_note': _('ゴミ関連備考'),
            'private_note': _('非公開建物備考'),
            'management_note': _('管理備考'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['postal_code'].widget.attrs['placeholder'] = '例: 999-9999'

        self.fields['pref'].widget.attrs['v-model'] = 'pref'
        self.fields['pref'].widget.attrs['v-on:change'] = 'changePref($event)'
        self.fields['city'].widget.attrs['v-model'] = 'city'
        self.fields['city'].widget.attrs['v-on:change'] = 'changeCity($event)'
        self.fields['town_address'].widget.attrs['v-model'] = 'townAddress'
        self.fields['town_name'].widget.attrs['v-model'] = 'townName'
        self.fields['area'].widget.attrs['v-model'] = 'area'
        self.fields['elementary_school'].widget.attrs['v-model'] = 'elementarySchool'
        self.fields['junior_high_school'].widget.attrs['v-model'] = 'juniorHighSchool'
        self.fields['around_note'].widget = forms.Textarea()
        self.fields['garage_note'].widget = forms.Textarea()
        self.fields['bike_parking_note'].widget = forms.Textarea()
        self.fields['department'].widget = forms.HiddenInput()
        self.fields['department'].widget.attrs['v-model'] = 'department'
        self.fields['agency_department'].widget = forms.HiddenInput()
        self.fields['agency_department'].widget.attrs['v-model'] = 'agencyDepartment'
        self.fields['staff1'].widget = forms.HiddenInput()
        self.fields['staff1'].widget.attrs['v-model'] = 'staff1'
        self.fields['staff2'].widget = forms.HiddenInput()
        self.fields['staff2'].widget.attrs['v-model'] = 'staff2'
        self.fields['owner'].widget = forms.HiddenInput()
        self.fields['owner'].widget.attrs['v-model'] = 'owner'
        self.fields['owner_note'].widget = forms.Textarea()
        self.fields['trader'].widget = forms.HiddenInput()
        self.fields['trader'].widget.attrs['v-model'] = 'trader'
        self.fields['building_management_note'].widget = forms.Textarea()
        self.fields['vacancy_portal_note'].widget = forms.Textarea()

        for i in range(1, 4):
            self.fields['railway' + str(i)] = forms.ModelChoiceField(
                label=_('沿線' + str(i)),
                queryset=Railway.objects.filter(
                    Q(is_trading=True, is_stopped=False)
                ).order_by('priority').all(),
                required=False,
            )
            self.fields['railway' + str(i)].widget.attrs['v-model'] = 'railway' + str(i)
            self.fields['railway' + str(i)].widget.attrs['v-on:change'] = 'changeRailway{id}($event)'.format(id=str(i))
            self.fields['station' + str(i)].widget.attrs['v-model'] = 'station' + str(i)

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']
        if postal_code:
            if not re.match(r'^\d{3}-\d{4}$', postal_code):
                raise forms.ValidationError('郵便番号は999-9999の形式で入力してください')
        return postal_code
