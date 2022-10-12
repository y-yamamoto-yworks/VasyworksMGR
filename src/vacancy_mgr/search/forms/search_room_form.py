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
from enums.models import Pref
from masters.models import City, Area
from masters.models import Railway, Station
from enums.models import ManagementType
from enums.models import RentalType, LayoutType
from enums.models import RoomAuthLevel
from enums.models import GarageType, BikeParkingType


class SearchRoomForm(forms.Form):
    """
    部屋検索フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 建物条件
        self.fields['building_name'] = forms.CharField(
            label=_('建物名称'),
            required=False,
        )

        self.fields['pref'] = forms.ModelChoiceField(
            label=_('都道府県'),
            queryset=Pref.objects.filter(
                Q(is_trading_area=True) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )
        self.fields['pref'].widget.attrs['v-model'] = 'pref'
        self.fields['pref'].widget.attrs['v-on:change'] = 'changePref($event)'

        self.fields['city'] = forms.ModelChoiceField(
            label=_('市区町村'),
            queryset=City.objects.filter(
                Q(is_trading_area=True, is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )
        self.fields['city'].widget.attrs['v-model'] = 'city'
        self.fields['city'].widget.attrs['v-on:change'] = 'changeCity($event)'

        self.fields['area'] = forms.ModelChoiceField(
            label=_('エリア'),
            queryset=Area.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('kana', 'id').all(),
            required=False,
        )
        self.fields['area'].widget.attrs['v-model'] = 'area'

        self.fields['railway'] = forms.ModelChoiceField(
            label=_('鉄道沿線'),
            queryset=Railway.objects.filter(
                Q(is_stopped=False, is_trading=True) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )
        self.fields['railway'].widget.attrs['v-model'] = 'railway'
        self.fields['railway'].widget.attrs['v-on:change'] = 'changeRailway($event)'

        self.fields['station'] = forms.ModelChoiceField(
            label=_('駅'),
            queryset=Station.objects.filter(
                Q(is_stopped=False, is_trading=True) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )
        self.fields['station'].widget.attrs['v-model'] = 'station'

        self.fields['lower_build_year'] = forms.IntegerField(
            label=_('築年下限'),
            required=False,
        )

        self.fields['upper_build_year'] = forms.IntegerField(
            label=_('築年上限'),
            required=False,
        )

        self.fields['management_type'] = forms.ModelChoiceField(
            label=_('管理種別'),
            queryset=ManagementType.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )

        self.fields['garage_type'] = forms.ModelChoiceField(
            label=_('駐車場'),
            queryset=GarageType.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )

        self.fields['bike_parking_type'] = forms.ModelChoiceField(
            label=_('駐輪場'),
            queryset=BikeParkingType.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )

        self.fields['building_is_hidden_vacancy'] = forms.ChoiceField(
            label=_('空室掲載'),
            choices=(
                ('0', '指定なし'),
                ('1', '掲載'),
                ('2', '非掲載'),
            ),
            required=True,
        )

        self.fields['building_is_vacancy_recommend'] = forms.ChoiceField(
            label=_('おすすめ掲載'),
            choices=(
                ('0', '指定なし'),
                ('1', '掲載'),
                ('2', '非掲載'),
            ),
            required=True,
        )

        self.fields['building_is_hidden_web'] = forms.ChoiceField(
            label=_('WEB掲載'),
            choices=(
                ('0', '指定なし'),
                ('1', '掲載'),
                ('2', '非掲載'),
            ),
            required=True,
        )

        # 部屋条件
        self.fields['lower_rent'] = forms.IntegerField(
            label=_('賃料下限'),
            required=False,
        )

        self.fields['upper_rent'] = forms.IntegerField(
            label=_('賃料上限'),
            required=False,
        )

        self.fields['rental_type'] = forms.ModelChoiceField(
            label=_('賃貸種別'),
            queryset=RentalType.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )

        self.fields['is_sublease'] = forms.ChoiceField(
            label=_('サブリース'),
            choices=(
                ('0', '指定なし'),
                ('1', '該当'),
                ('2', '非該当'),
            ),
            required=True,
        )

        self.fields['is_condo_management'] = forms.ChoiceField(
            label=_('分譲管理'),
            choices=(
                ('0', '指定なし'),
                ('1', '該当'),
                ('2', '非該当'),
            ),
            required=True,
        )

        self.fields['is_entrusted'] = forms.ChoiceField(
            label=_('専任'),
            choices=(
                ('0', '指定なし'),
                ('1', '該当'),
                ('2', '非該当'),
            ),
            required=True,
        )

        self.fields['room_status_category'] = forms.ChoiceField(
            label=_('部屋状況'),
            choices=(
                ('0', '指定なし'),
                ('10', '募集中'),
                ('11', '空室'),
                ('12', '解約予定'),
                ('20', '募集停止'),
                ('21', '保留中'),
            ),
            required=True,
        )

        self.fields['layout_type'] = forms.ModelChoiceField(
            label=_('間取り'),
            queryset=LayoutType.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )

        self.fields['lower_room_auth_level'] = forms.ModelChoiceField(
            label=_('閲覧レベル下限'),
            queryset=RoomAuthLevel.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )

        self.fields['upper_room_auth_level'] = forms.ModelChoiceField(
            label=_('閲覧レベル上限'),
            queryset=RoomAuthLevel.objects.filter(
                Q(is_stopped=False) | Q(pk=0)
            ).order_by('priority', 'id').all(),
            required=False,
        )

        self.fields['room_is_publish_vacancy'] = forms.ChoiceField(
            label=_('空室掲載'),
            choices=(
                ('0', '指定なし'),
                ('1', '掲載'),
                ('2', '非掲載'),
            ),
            required=True,
        )

        self.fields['room_is_publish_web'] = forms.ChoiceField(
            label=_('WEB掲載'),
            choices=(
                ('0', '指定なし'),
                ('1', '掲載'),
                ('2', '非掲載'),
            ),
            required=True,
        )

        for key in self.fields.keys():
            field = self.fields[key]
            field.widget.attrs['ref'] = key
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
