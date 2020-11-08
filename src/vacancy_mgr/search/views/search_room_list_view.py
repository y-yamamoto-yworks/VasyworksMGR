"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from abc import ABCMeta, abstractmethod
from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, escape_uri_path
from django.utils.translation import gettext_lazy as _
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, FormView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from dateutil.relativedelta import relativedelta
from PIL import Image
from lib.convert import *
from lib.functions import *
from api.api_helper import ApiHelper
from enums.models import Pref
from enums.models import ManagementType
from enums.models import GarageType, BikeParkingType
from enums.models import RentalType, LayoutType
from enums.models import RoomAuthLevel
from masters.models import City, Area
from masters.models import Railway, Station
from property.models import Room
from search.forms import SearchRoomForm


class SearchRoomListView(FormView):
    """
    部屋検索
    """
    form_class = SearchRoomForm
    template_name = 'search/search_room_list.html'
    user = None
    is_searched = False
    building_name = None
    pref = None
    city = None
    area = None
    railway = None
    station = None
    lower_build_year = None
    upper_build_year = None
    management_type = None
    garage_type = None
    bike_parking_type = None
    building_is_hidden_vacancy = None
    building_is_vacancy_recommend = None
    building_is_hidden_web = None
    lower_rent = None
    upper_rent = None
    rental_type = None
    is_sublease = None
    is_condo_management = None
    is_entrusted = None
    room_status_category = None
    layout_type = None
    lower_room_auth_level = None
    upper_room_auth_level = None
    room_is_publish_vacancy = None
    room_is_publish_web = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        if not self.room_status_category:
            initial['room_status_category'] = '10'     # 募集中
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['api_key'] = ApiHelper.get_key()
        context['is_searched'] = self.is_searched
        context['condo_fees_name'] = settings.CONDO_FEES_NAME

        if self.is_searched:
            conditions = Q(is_deleted=False, building__is_deleted=False)

            # 建物条件
            if self.building_name:
                conditions.add(Q(building__building_name__contains=self.building_name), Q.AND)

            if self.area:
                conditions.add(Q(building__area=self.area), Q.AND)
            elif self.city:
                conditions.add(Q(building__city=self.city), Q.AND)
            elif self.pref:
                conditions.add(Q(building__pref=self.pref), Q.AND)

            if self.station:
                conditions.add(Q(
                    Q(building__station1=self.station)
                    | Q(building__station2=self.station)
                    | Q(building__station3=self.station)
                ), Q.AND)

            if self.lower_build_year:
                conditions.add(Q(building__build_year__gte=self.lower_build_year), Q.AND)
            if self.upper_build_year:
                conditions.add(Q(building__build_year__lte=self.upper_build_year), Q.AND)

            if self.management_type:
                conditions.add(Q(building__management_type=self.management_type), Q.AND)

            if self.garage_type:
                conditions.add(Q(building__garage_type=self.garage_type), Q.AND)

            if self.bike_parking_type:
                conditions.add(Q(building__bike_parking_type=self.bike_parking_type), Q.AND)

            if self.building_is_hidden_vacancy == '1':
                conditions.add(Q(building__is_hidden_vacancy=False), Q.AND)
            elif self.building_is_hidden_vacancy == '2':
                conditions.add(Q(building__is_hidden_vacancy=True), Q.AND)

            if self.building_is_vacancy_recommend == '1':
                conditions.add(Q(building__is_vacancy_recommend=True), Q.AND)
            elif self.building_is_vacancy_recommend == '2':
                conditions.add(Q(building__is_vacancy_recommend=False), Q.AND)

            if self.building_is_hidden_web == '1':
                conditions.add(Q(building__is_hidden_web=False), Q.AND)
            elif self.building_is_hidden_web == '2':
                conditions.add(Q(building__is_hidden_web=True), Q.AND)

            # 部屋条件
            if self.lower_rent:
                conditions.add(Q(rent__gte=self.lower_rent), Q.AND)
            if self.upper_rent:
                conditions.add(Q(rent__lte=self.upper_rent), Q.AND)

            if self.rental_type:
                conditions.add(Q(rental_type=self.rental_type), Q.AND)

            if self.is_sublease == '1':
                conditions.add(Q(is_sublease=True), Q.AND)
            elif self.is_sublease == '2':
                conditions.add(Q(is_sublease=False), Q.AND)

            if self.is_condo_management == '1':
                conditions.add(Q(is_condo_management=True), Q.AND)
            elif self.is_condo_management == '2':
                conditions.add(Q(is_condo_management=False), Q.AND)

            if self.is_entrusted == '1':
                conditions.add(Q(is_entrusted=True), Q.AND)
            elif self.is_entrusted == '2':
                conditions.add(Q(is_entrusted=False), Q.AND)

            if self.room_status_category == '10':
                conditions.add(Q(room_status__for_rent=True), Q.AND)
            elif self.room_status_category == '11':
                conditions.add(Q(room_status__for_rent=True, room_status__will_be_canceled=False), Q.AND)
            elif self.room_status_category == '12':
                conditions.add(Q(room_status__will_be_canceled=True), Q.AND)
            elif self.room_status_category == '20':
                conditions.add(Q(room_status__for_rent=False), Q.AND)
            elif self.room_status_category == '21':
                conditions.add(Q(room_status__is_pending=True), Q.AND)

            if self.layout_type:
                conditions.add(Q(layout_type=self.layout_type), Q.AND)

            if self.lower_room_auth_level:
                conditions.add(Q(room_auth_level__level__gte=self.lower_room_auth_level.level), Q.AND)
            if self.upper_room_auth_level:
                conditions.add(Q(room_auth_level__level__lte=self.upper_room_auth_level.level), Q.AND)

            if self.room_is_publish_vacancy == '1':
                conditions.add(Q(is_publish_vacancy=True), Q.AND)
            elif self.room_is_publish_vacancy == '2':
                conditions.add(Q(is_publish_vacancy=False), Q.AND)

            if self.room_is_publish_web == '1':
                conditions.add(Q(is_publish_web=True), Q.AND)
            elif self.room_is_publish_web == '2':
                conditions.add(Q(is_publish_web=False), Q.AND)

            rooms = Room.objects.filter(conditions).order_by(
                'building__pref__priority',
                'building__city__priority',
                'building__building_kana',
                'building__id',
                'room_no',
                'id',
            ).all()
            context['rooms'] = rooms

        else:
            context['is_searched'] = False

        if settings.DEFAULT_PREF_ID:
            context['default_pref_id'] = settings.DEFAULT_PREF_ID

        return context

    def form_valid(self, form):
        if self.request.method in ('POST', 'PUT'):
            self.is_searched = True

            # 建物条件
            data = form.data.get('building_name')
            if data:
                self.building_name = data

            data = form.data.get('pref')
            if data and data != '0':
                self.pref = Pref.objects.get(pk=data)

            data = form.data.get('city')
            if data and data != '0':
                self.city = City.objects.get(pk=data)

            data = form.data.get('area')
            if data and data != '0':
                self.area = Area.objects.get(pk=data)

            data = form.data.get('railway')
            if data and data != '0':
                self.railway = Railway.objects.get(pk=data)

            data = form.data.get('station')
            if data and data != '0':
                self.station = Station.objects.get(pk=data)

            data = xint(form.data.get('lower_build_year'))
            if data > 0:
                self.lower_build_year = data

            data = xint(form.data.get('upper_build_year'))
            if data > 0:
                self.upper_build_year = data

            data = form.data.get('management_type')
            if data and data != '0':
                self.management_type = ManagementType.objects.get(pk=data)

            data = form.data.get('garage_type')
            if data:    # 無しも検索対象
                self.garage_type = GarageType.objects.get(pk=data)

            data = form.data.get('bike_parking_type')
            if data:    # 無しも検索対象
                self.bike_parking_type = BikeParkingType.objects.get(pk=data)

            data = form.data.get('building_is_hidden_vacancy')
            if data and data != '0':
                self.building_is_hidden_vacancy = data

            data = form.data.get('building_is_vacancy_recommend')
            if data and data != '0':
                self.building_is_vacancy_recommend = data

            data = form.data.get('building_is_hidden_web')
            if data and data != '0':
                self.building_is_hidden_web = data

            # 部屋条件
            data = xint(form.data.get('lower_rent'))
            if data > 0:
                self.lower_rent = data

            data = xint(form.data.get('upper_rent'))
            if data > 0:
                self.upper_rent = data

            data = form.data.get('rental_type')
            if data and data != '0':
                self.rental_type = RentalType.objects.get(pk=data)

            data = form.data.get('is_sublease')
            if data and data != '0':
                self.is_sublease = data

            data = form.data.get('is_condo_management')
            if data and data != '0':
                self.is_condo_management = data

            data = form.data.get('is_entrusted')
            if data and data != '0':
                self.is_entrusted = data

            data = form.data.get('room_status_category')
            if data and data != '0':
                self.room_status_category = data

            data = form.data.get('layout_type')
            if data and data != '0':
                self.layout_type = LayoutType.objects.get(pk=data)

            data = form.data.get('lower_room_auth_level')
            if data and data != '0':
                self.lower_room_auth_level = RoomAuthLevel.objects.get(pk=data)

            data = form.data.get('upper_room_auth_level')
            if data and data != '0':
                self.upper_room_auth_level = RoomAuthLevel.objects.get(pk=data)

            data = form.data.get('room_is_publish_vacancy')
            if data and data != '0':
                self.room_is_publish_vacancy = data

            data = form.data.get('room_is_publish_web')
            if data and data != '0':
                self.room_is_publish_web = data

        return self.render_to_response(self.get_context_data())
