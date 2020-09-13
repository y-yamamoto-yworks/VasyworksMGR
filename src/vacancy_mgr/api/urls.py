"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from django.views.generic import TemplateView
from api.viewsets import *

urlpatterns = [
    path('areas/<str:key>/<int:city_id>', AreaViewSet.as_view({'get': 'list'}), name='api_areas'),
    path('cities/<str:key>/<int:pref_id>', CityViewSet.as_view({'get': 'list'}), name='api_cities'),
    path('departments/<str:key>', DepartmentViewSet.as_view({'get': 'list'}), name='api_departments'),
    path('departments/<str:key>/<str:hint>', DepartmentViewSet.as_view({'get': 'list'}), name='api_departments_with_hint'),
    path('elementary_schools/<str:key>/<int:city_id>', ElementarySchoolViewSet.as_view({'get': 'list'}), name='api_elementary_schools'),
    path('guarantee_companies/<str:key>', GuaranteeCompanyViewSet.as_view({'get': 'list'}), name='api_guarantee_company'),
    path('insurance_companies/<str:key>', InsuranceCompanyViewSet.as_view({'get': 'list'}), name='api_insurance_company'),
    path('junior_high_schools/<str:key>/<int:city_id>', JuniorHighSchoolViewSet.as_view({'get': 'list'}), name='api_junior_high_schools'),
    path('landmark_types/<str:key>/', LandmarkTypeViewSet.as_view({'get': 'list'}), name='api_landmark_types'),
    path('landmarks/<str:key>/<int:landmark_type_id>', LandmarkViewSet.as_view({'get': 'list'}), name='api_landmarks'),
    path('new_key/<str:key>/', NewKeyViewSet.as_view({'get': 'retrieve'}), name='api_new_key'),
    path('owners/<str:key>', OwnerViewSet.as_view({'get': 'list'}), name='api_owners'),
    path('owners/<str:key>/<str:hint>', OwnerViewSet.as_view({'get': 'list'}), name='api_owners_with_hint'),
    path('postal_code/<str:key>/<str:postal_code>', PostalCodeViewSet.as_view({'get': 'retrieve'}), name='api_postal_code'),
    path('prefs/<str:key>/', PrefViewSet.as_view({'get': 'list'}), name='api_prefs'),
    path('railways/<str:key>/', RailwayViewSet.as_view({'get': 'list'}), name='api_railways'),
    path('room_pictures/<str:key>/<int:id>', RoomPictureViewSet.as_view({'get': 'list'}), name='api_room_pictures'),
    path('staffs/<str:key>', StaffViewSet.as_view({'get': 'list'}), name='api_staffs'),
    path('staffs/<str:key>/<str:hint>', StaffViewSet.as_view({'get': 'list'}), name='api_staffs_with_hint'),
    path('stations/<str:key>/<int:railway_id>', StationViewSet.as_view({'get': 'list'}), name='api_stations'),
    path('traders/<str:key>', TraderViewSet.as_view({'get': 'list'}), name='api_traders'),
    path('traders/<str:key>/<str:hint>', TraderViewSet.as_view({'get': 'list'}), name='api_traders_with_hint'),
    path('vacancy_input_bike_parkings/<str:key>', VacancyInputBikeParkingViewSet.as_view({'get': 'list'}), name='api_vacancy_input_bike_parkings'),
    path('vacancy_input_cancel_notices/<str:key>', VacancyInputCancelNoticeViewSet.as_view({'get': 'list'}), name='api_vacancy_input_cancel_notices'),
    path('vacancy_input_change_locks/<str:key>', VacancyInputChangeLockViewSet.as_view({'get': 'list'}), name='api_vacancy_input_change_locks'),
    path('vacancy_input_cleanings/<str:key>', VacancyInputCleaningViewSet.as_view({'get': 'list'}), name='api_vacancy_input_cleanings'),
    path('vacancy_input_document_prices/<str:key>', VacancyInputDocumentPriceViewSet.as_view({'get': 'list'}), name='api_vacancy_input_document_prices'),
    path('vacancy_input_electrics/<str:key>', VacancyInputElectricViewSet.as_view({'get': 'list'}), name='api_vacancy_input_electrics'),
    path('vacancy_input_garages/<str:key>', VacancyInputGarageViewSet.as_view({'get': 'list'}), name='api_vacancy_input_garages'),
    path('vacancy_input_gases/<str:key>', VacancyInputGasViewSet.as_view({'get': 'list'}), name='api_vacancy_input_gases'),
    path('vacancy_input_guarantees/<str:key>', VacancyInputGuaranteeViewSet.as_view({'get': 'list'}), name='api_vacancy_input_guarantees'),
    path('vacancy_input_guarantor_limits/<str:key>', VacancyInputGuarantorLimitViewSet.as_view({'get': 'list'}), name='api_vacancy_input_guarantor_limits'),
    path('vacancy_input_insurances/<str:key>', VacancyInputInsuranceViewSet.as_view({'get': 'list'}), name='api_vacancy_input_insurances'),
    path('vacancy_input_internets/<str:key>', VacancyInputInternetViewSet.as_view({'get': 'list'}), name='api_vacancy_input_internets'),
    path('vacancy_input_payments/<str:key>', VacancyInputPaymentViewSet.as_view({'get': 'list'}), name='api_vacancy_input_payments'),
    path('vacancy_input_portals/<str:key>', VacancyInputPortalViewSet.as_view({'get': 'list'}), name='api_vacancy_input_portals'),
    path('vacancy_input_renewal_charges/<str:key>', VacancyInputRenewalChargeViewSet.as_view({'get': 'list'}), name='api_vacancy_input_renewal_charges'),
    path('vacancy_input_short_cancels/<str:key>', VacancyInputShortCancelViewSet.as_view({'get': 'list'}), name='api_vacancy_input_short_cancels'),
    path('vacancy_input_waters/<str:key>', VacancyInputWaterViewSet.as_view({'get': 'list'}), name='api_vacancy_input_waters'),
    path('vacancy_themes/<str:key>', VacancyThemeViewSet.as_view({'get': 'list'}), name='api_vacancy_themes'),

    path('', TemplateView.as_view(template_name='404.html'), name='api_index'),
]
