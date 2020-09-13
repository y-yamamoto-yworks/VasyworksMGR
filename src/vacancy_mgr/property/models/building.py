"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *
from users.models import User
from company.models import Department, Staff
from enums.models import Pref
from enums.models import ManagementType, BuildingType, Structure
from enums.models import ArrivalType, TaxType
from enums.models import BikeParkingType, GarageType, GarageStatus
from enums.models import Existence
from masters.models import Area, City
from masters.models import ElementarySchool, JuniorHighSchool
from masters.models import Station
from owner.models import Owner
from trader.models import Trader


class Building(models.Model):
    """
    建物
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    oid = models.CharField(_('oid'), db_column='oid', db_index=True, unique=True, max_length=50)
    file_oid = models.CharField(_('file_oid'), db_column='file_oid', db_index=True, unique=True, max_length=50)
    building_code = models.CharField(_('building_code'), db_column='building_code', max_length=20, db_index=True, null=True, blank=True)
    building_name = models.CharField(_('building_name'), db_column='building_name', max_length=100, db_index=True, null=True, blank=True)
    building_kana = models.CharField(_('building_kana'), db_column='building_kana', max_length=100, db_index=True, null=True, blank=True)
    building_old_name = models.CharField(_('building_old_name'), db_column='building_old_name', max_length=100, null=True, blank=True)

    postal_code = models.CharField(_('postal_code'), db_column='postal_code', max_length=10, null=True, blank=True)
    pref = models.ForeignKey(
        Pref,
        db_column='pref_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading_area=True) | Q(pk=0),
    )
    city = models.ForeignKey(
        City,
        db_column='city_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading_area=True, is_stopped=False) | Q(pk=0),
    )
    town_address = models.CharField(_('town_address'), db_column='town_address', max_length=255, null=True, blank=True)
    town_name = models.CharField(_('town_name'), db_column='town_name', max_length=100, null=True, blank=True)
    house_no = models.CharField(_('house_no'), db_column='house_no', max_length=100, null=True, blank=True)
    building_no = models.CharField(_('building_no'), db_column='building_no', max_length=100, null=True, blank=True)
    lat = models.FloatField(_('lat'), db_column='lat', db_index=True, default=0)
    lng = models.FloatField(_('lng'), db_column='lng', db_index=True, default=0)
    area = models.ForeignKey(
        Area,
        db_column='area_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )

    elementary_school = models.ForeignKey(
        ElementarySchool,
        db_column='elementary_school_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )
    elementary_school_distance = models.IntegerField(_('elementary_school_distance'), db_column='elementary_school_distance', default=0)

    junior_high_school = models.ForeignKey(
        JuniorHighSchool,
        db_column='junior_high_school_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )
    junior_high_school_distance = models.IntegerField(_('junior_high_school_distance'), db_column='junior_high_school_distance', default=0)
    around_note = models.CharField(_('around_note'), db_column='around_note', max_length=255, null=True, blank=True)

    management_type = models.ForeignKey(
        ManagementType,
        db_column='management_type_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    department = models.ForeignKey(
        Department,
        db_column='department_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    staff1 = models.ForeignKey(
        Staff,
        db_column='staff_id1',
        related_name='staff1_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    staff2 = models.ForeignKey(
        Staff,
        db_column='staff_id2',
        related_name='staff2_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    priority_level = models.IntegerField(_('priority_level'), db_column='priority_level', db_index=True, default=50)
    agency_department = models.ForeignKey(
        Department,
        db_column='agency_department_id',
        related_name='agency_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )

    owner = models.ForeignKey(
        Owner,
        db_column='owner_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    owner_note = models.CharField(_('owner_note'), db_column='owner_note', max_length=255, null=True, blank=True)
    trader = models.ForeignKey(
        Trader,
        db_column='trader_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    register_address = models.CharField(_('register_address'), db_column='register_address', max_length=255, null=True, blank=True)
    register_name = models.CharField(_('register_name'), db_column='register_name', max_length=255, null=True, blank=True)
    register_building_no = models.CharField(_('register_building_no'), db_column='register_building_no', max_length=255, null=True, blank=True)
    register_no = models.CharField(_('register_no'), db_column='register_no', max_length=50, null=True, blank=True)

    arrival_type1 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id1',
        related_name='buildings1',
        on_delete=models.PROTECT,
        default=0,
    )
    station1 = models.ForeignKey(
        Station,
        db_column='station_id1',
        related_name='buildings1',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading=True, is_stopped=False) | Q(pk=0),
    )
    station_time1 = models.IntegerField(_('station_time1'), db_column='station_time1', default=0)
    bus_stop1 = models.CharField(_('bus_stop1'), db_column='bus_stop1', max_length=50, null=True, blank=True)
    bus_stop_time1 = models.IntegerField(_('bus_stop_time1'), db_column='bus_stop_time1', default=0)

    arrival_type2 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id2',
        related_name='buildings2',
        on_delete=models.PROTECT,
        default=0,
    )
    station2 = models.ForeignKey(
        Station,
        db_column='station_id2',
        related_name='buildings2',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading=True, is_stopped=False) | Q(pk=0),
    )
    station_time2 = models.IntegerField(_('station_time2'), db_column='station_time2', default=0)
    bus_stop2 = models.CharField(_('bus_stop2'), db_column='bus_stop2', max_length=50, null=True, blank=True)
    bus_stop_time2 = models.IntegerField(_('bus_stop_time2'), db_column='bus_stop_time2', default=0)

    arrival_type3 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id3',
        related_name='buildings3',
        on_delete=models.PROTECT,
        default=0,
    )
    station3 = models.ForeignKey(
        Station,
        db_column='station_id3',
        related_name='buildings3',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading=True, is_stopped=False) | Q(pk=0),
    )
    station_time3 = models.IntegerField(_('station_time3'), db_column='station_time3', default=0)
    bus_stop3 = models.CharField(_('bus_stop3'), db_column='bus_stop3', max_length=50, null=True, blank=True)
    bus_stop_time3 = models.IntegerField(_('bus_stop_time3'), db_column='bus_stop_time3', default=0)

    building_type = models.ForeignKey(
        BuildingType,
        db_column='building_type_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    building_type_comment = models.CharField(_('building_type_comment'), db_column='building_type_comment', max_length=100, null=True, blank=True)
    structure = models.ForeignKey(
        Structure,
        db_column='structure_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    structure_comment = models.CharField(_('structure_comment'), db_column='structure_comment', max_length=100, null=True, blank=True)
    building_rooms = models.IntegerField(_('building_rooms'), db_column='building_rooms', default=0)
    building_floors = models.IntegerField(_('building_floors'), db_column='building_floors', default=0)
    building_undergrounds = models.IntegerField(_('building_undergrounds'), db_column='building_undergrounds', default=0)
    build_year = models.IntegerField(_('build_year'), db_column='build_year', db_index=True, default=1970)
    build_month = models.IntegerField(_('build_month'), db_column='build_month', default=1)

    bike_parking_type = models.ForeignKey(
        BikeParkingType,
        db_column='bike_parking_type_id',
        related_name='buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    with_bike_parking_roof = models.BooleanField(_('with_bike_parking_roof'), db_column='with_bike_parking_roof', default=False)
    bike_parking_fee_lower = models.IntegerField(_('bike_parking_fee_lower'), db_column='bike_parking_fee_lower', default=0)
    bike_parking_fee_upper = models.IntegerField(_('bike_parking_fee_upper'), db_column='bike_parking_fee_upper', default=0)
    bike_parking_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='bike_parking_fee_tax_type_id',
        related_name='bike_parking_fee_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    bike_parking_note = models.CharField(_('bike_parking_note'), db_column='bike_parking_note', max_length=255, null=True, blank=True)
    garage_type = models.ForeignKey(
        GarageType,
        db_column='garage_type_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    garage_status = models.ForeignKey(
        GarageStatus,
        db_column='garage_status_id',
        related_name='buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_distance = models.IntegerField(_('garage_distance'), db_column='garage_distance', default=0)
    garage_fee_lower = models.IntegerField(_('garage_fee_lower'), db_column='garage_fee_lower', default=0)
    garage_fee_upper = models.IntegerField(_('garage_fee_upper'), db_column='garage_fee_upper', default=0)
    garage_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='garage_fee_tax_type_id',
        related_name='garage_fee_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_charge_lower = models.IntegerField(_('garage_charge_lower'), db_column='garage_charge_lower', default=0)
    garage_charge_upper = models.IntegerField(_('garage_charge_upper'), db_column='garage_charge_upper', default=0)
    garage_charge_tax_type = models.ForeignKey(
        TaxType,
        db_column='garage_charge_tax_type_id',
        related_name='garage_charge_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_note = models.CharField(_('garage_note'), db_column='garage_note', max_length=255, null=True, blank=True)
    building_management_company = models.CharField(_('building_management_company'), db_column='building_management_company', max_length=100, null=True, blank=True)
    building_management_address = models.CharField(_('building_management_address'), db_column='building_management_address', max_length=255, null=True, blank=True)
    building_management_tel = models.CharField(_('building_management_tel'), db_column='building_management_tel', max_length=20, null=True, blank=True)
    building_management_no = models.CharField(_('building_management_no'), db_column='building_management_no', max_length=50, null=True, blank=True)
    building_management_note = models.CharField(_('building_management_note'), db_column='building_management_note', max_length=255, null=True, blank=True)

    agreement_existence = models.ForeignKey(
        Existence,
        db_column='agreement_existence_id',
        related_name='agreement_existence_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    apartment_manager_comment = models.CharField(_('apartment_manager_comment'), db_column='apartment_manager_comment', max_length=100, null=True, blank=True)

    auto_lock_no = models.CharField(_('auto_lock_no'), db_column='auto_lock_no', max_length=20, null=True, blank=True)

    is_hidden_vacancy = models.BooleanField(_('is_hidden_vacancy'), db_column='is_hidden_vacancy', db_index=True, default=False)
    is_vacancy_recommend = models.BooleanField(_('is_vacancy_recommend'), db_column='is_vacancy_recommend', db_index=True, default=False)
    vacancy_rent_comment = models.CharField(_('vacancy_rent_comment'), db_column='vacancy_rent_comment', max_length=100, null=True, blank=True)
    vacancy_condo_fees_comment = models.CharField(_('vacancy_condo_fees_comment'), db_column='vacancy_condo_fees_comment', max_length=100, null=True, blank=True)
    vacancy_water_comment = models.CharField(_('vacancy_water_comment'), db_column='vacancy_water_comment', max_length=100, null=True, blank=True)
    vacancy_electric_comment = models.CharField(_('vacancy_electric_comment'), db_column='vacancy_electric_comment', max_length=100, null=True, blank=True)
    vacancy_gas_comment = models.CharField(_('vacancy_gas_comment'), db_column='vacancy_gas_comment', max_length=100, null=True, blank=True)
    vacancy_internet_comment = models.CharField(_('vacancy_internet_comment'), db_column='vacancy_internet_comment', max_length=100, null=True, blank=True)
    vacancy_cancel_notice_comment = models.CharField(_('vacancy_cancel_notice_comment'), db_column='vacancy_cancel_notice_comment', max_length=100, null=True, blank=True)
    vacancy_short_cancel_comment = models.CharField(_('vacancy_short_cancel_comment'), db_column='vacancy_short_cancel_comment', max_length=100, null=True, blank=True)
    vacancy_payment_comment = models.CharField(_('vacancy_payment_comment'), db_column='vacancy_payment_comment', max_length=100, null=True, blank=True)
    vacancy_guarantee_comment = models.CharField(_('vacancy_guarantee_comment'), db_column='vacancy_guarantee_comment', max_length=100, null=True, blank=True)
    vacancy_insurance_comment = models.CharField(_('vacancy_insurance_comment'), db_column='vacancy_insurance_comment', max_length=100, null=True, blank=True)
    vacancy_guarantor_limit_comment = models.CharField(_('vacancy_guarantor_limit_comment'), db_column='vacancy_guarantor_limit_comment', max_length=100, null=True, blank=True)
    vacancy_document_price_comment = models.CharField(_('vacancy_document_price_comment'), db_column='vacancy_document_price_comment', max_length=100, null=True, blank=True)
    vacancy_renewal_fee_comment = models.CharField(_('vacancy_renewal_fee_comment'), db_column='vacancy_renewal_fee_comment', max_length=100, null=True, blank=True)
    vacancy_renewal_charge_comment = models.CharField(_('vacancy_renewal_charge_comment'), db_column='vacancy_renewal_charge_comment', max_length=100, null=True, blank=True)
    vacancy_auto_lock_comment = models.CharField(_('vacancy_auto_lock_comment'), db_column='vacancy_auto_lock_comment', max_length=100, null=True, blank=True)
    vacancy_security_comment = models.CharField(_('vacancy_security_comment'), db_column='vacancy_security_comment', max_length=100, null=True, blank=True)
    vacancy_bike_parking_comment = models.CharField(_('vacancy_bike_parking_comment'), db_column='vacancy_bike_parking_comment', max_length=100, null=True, blank=True)
    vacancy_garage_comment = models.CharField(_('vacancy_garage_comment'), db_column='vacancy_garage_comment', max_length=100, null=True, blank=True)
    vacancy_cleaning_comment = models.CharField(_('vacancy_cleaning_comment'), db_column='vacancy_cleaning_comment', max_length=100, null=True, blank=True)
    vacancy_change_lock_comment = models.CharField(_('vacancy_change_lock_comment'), db_column='vacancy_change_lock_comment', max_length=100, null=True, blank=True)
    vacancy_portal_note = models.CharField(_('vacancy_portal_note'), db_column='vacancy_portal_note', max_length=255, null=True, blank=True)
    vacancy_catch_copy = models.CharField(_('vacancy_catch_copy'), db_column='vacancy_catch_copy', max_length=100, null=True, blank=True)
    vacancy_appeal = models.CharField(_('vacancy_appeal'), db_column='vacancy_appeal', max_length=255, null=True, blank=True)
    vacancy_note = models.TextField(_('vacancy_note'), db_column='vacancy_note', max_length=2000, null=True, blank=True)

    is_hidden_web = models.BooleanField(_('is_hidden_web'), db_column='is_hidden_web', db_index=True, default=False)
    web_catch_copy = models.CharField(_('web_catch_copy'), db_column='web_catch_copy', max_length=100, null=True, blank=True)
    web_appeal = models.CharField(_('web_appeal'), db_column='web_appeal', max_length=255, null=True, blank=True)
    web_note = models.TextField(_('web_note'), db_column='web_note', max_length=2000, null=True, blank=True)

    tenant_note = models.TextField(_('tenant_note'), db_column='tenant_note', max_length=2000, null=True, blank=True)
    garbage_note = models.TextField(_('garbage_note'), db_column='garbage_note', max_length=2000, null=True, blank=True)
    private_note = models.TextField(_('private_note'), db_column='private_note', max_length=2000, null=True, blank=True)
    management_note = models.TextField(_('management_note'), db_column='management_note', max_length=2000, null=True, blank=True)

    created_at = models.DateTimeField(_('created_at'), db_column='created_at', default=timezone.now)
    created_user = models.ForeignKey(
        User,
        db_column='created_user_id',
        related_name='created_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    updated_at = models.DateTimeField(_('updated_at'), db_column='updated_at', default=timezone.now)
    updated_user = models.ForeignKey(
        User,
        db_column='updated_user_id',
        related_name='updated_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'building'
        ordering = ['building_kana', 'id']
        verbose_name = _('building')
        verbose_name_plural = _('buildings')

    def __str__(self):
        return self.building_name

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def address(self):
        ans = None
        if self.pref:
            ans = xstr(self.pref.name)
            if self.pref.id != 0 and self.city:
                ans += xstr(self.city.name)
                if self.city.id != 0:
                    ans += xstr(self.town_address)
                    ans += xstr(self.house_no)
                    if self.building_no:
                        ans += ' ' + xstr(self.building_no)
        return ans

    @property
    def nearest_station1(self):
        ans = None
        if self.station1:
            if self.station1.id != 0:
                ans = xstr(self.station1.railway.name) + ' ' + xstr(self.station1.name)
                ans += ' 駅まで' + xstr(self.arrival_type1.name)
                ans += xstr(self.station_time1) + '分'
                if xint(self.arrival_type1.id) == 2:
                    ans += '（バス停 ' + xstr(self.bus_stop1)
                    if xint(self.bus_stop_time1) > 0:
                        ans += 'まで徒歩' + xstr(self.bus_stop_time1) + '分'
                    ans += '）'
        return ans

    @property
    def nearest_station2(self):
        ans = None
        if self.station2:
            if self.station2.id != 0:
                ans = xstr(self.station2.railway.name) + ' ' + xstr(self.station2.name)
                ans += ' 駅まで' + xstr(self.arrival_type2.name)
                ans += xstr(self.station_time2) + '分'
                if xint(self.arrival_type2.id) == 2:
                    ans += '（バス停 ' + xstr(self.bus_stop2)
                    if xint(self.bus_stop_time2) > 0:
                        ans += 'まで徒歩' + xstr(self.bus_stop_time2) + '分'
                    ans += '）'
        return ans

    @property
    def nearest_station3(self):
        ans = None
        if self.station3:
            if self.station3.id != 0:
                ans = xstr(self.station3.railway.name) + ' ' + xstr(self.station3.name)
                ans += ' 駅まで' + xstr(self.arrival_type3.name)
                ans += xstr(self.station_time3) + '分'
                if xint(self.arrival_type3.id) == 2:
                    ans += '（バス停 ' + xstr(self.bus_stop3)
                    if xint(self.bus_stop_time3) > 0:
                        ans += 'まで徒歩' + xstr(self.bus_stop_time3) + '分'
                    ans += '）'
        return ans
