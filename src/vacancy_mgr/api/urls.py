"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
from django.urls import include, path
from django.views.generic import TemplateView
from api.viewsets import *

urlpatterns = [
    path('areas/<int:city_id>', AreaViewSet.as_view({'get': 'list'}), name='api_areas'),
    path('cities/<int:pref_id>', CityViewSet.as_view({'get': 'list'}), name='api_cities'),
    path('departments/', DepartmentViewSet.as_view({'get': 'list'}), name='api_departments'),
    path('departments/<str:hint>', DepartmentViewSet.as_view({'get': 'list'}), name='api_departments_with_hint'),
    path('elementary_schools/<int:city_id>', ElementarySchoolViewSet.as_view({'get': 'list'}), name='api_elementary_schools'),
    path('guarantee_companies/', GuaranteeCompanyViewSet.as_view({'get': 'list'}), name='api_guarantee_company'),
    path('insurance_companies/', InsuranceCompanyViewSet.as_view({'get': 'list'}), name='api_insurance_company'),
    path('junior_high_schools/<int:city_id>', JuniorHighSchoolViewSet.as_view({'get': 'list'}), name='api_junior_high_schools'),
    path('landmark_types/', LandmarkTypeViewSet.as_view({'get': 'list'}), name='api_landmark_types'),
    path('landmarks/<int:landmark_type_id>', LandmarkViewSet.as_view({'get': 'list'}), name='api_landmarks'),
    path('new_key/', NewKeyViewSet.as_view({'get': 'retrieve'}), name='api_new_key'),
    path('owners/', OwnerViewSet.as_view({'get': 'list'}), name='api_owners'),
    path('owners/<str:hint>', OwnerViewSet.as_view({'get': 'list'}), name='api_owners_with_hint'),
    path('postal_code/<str:postal_code>', PostalCodeViewSet.as_view({'get': 'retrieve'}), name='api_postal_code'),
    path('prefs/', PrefViewSet.as_view({'get': 'list'}), name='api_prefs'),
    path('railways/', RailwayViewSet.as_view({'get': 'list'}), name='api_railways'),
    path('room_pictures/<int:id>', RoomPictureViewSet.as_view({'get': 'list'}), name='api_room_pictures'),
    path('staffs/', StaffViewSet.as_view({'get': 'list'}), name='api_staffs'),
    path('staffs/<str:hint>', StaffViewSet.as_view({'get': 'list'}), name='api_staffs_with_hint'),
    path('stations/<int:railway_id>', StationViewSet.as_view({'get': 'list'}), name='api_stations'),
    path('traders/', TraderViewSet.as_view({'get': 'list'}), name='api_traders'),
    path('traders/<str:hint>', TraderViewSet.as_view({'get': 'list'}), name='api_traders_with_hint'),
    path('vacancy_input_bike_parkings/', VacancyInputBikeParkingViewSet.as_view({'get': 'list'}), name='api_vacancy_input_bike_parkings'),
    path('vacancy_input_cancel_notices/', VacancyInputCancelNoticeViewSet.as_view({'get': 'list'}), name='api_vacancy_input_cancel_notices'),
    path('vacancy_input_change_locks/', VacancyInputChangeLockViewSet.as_view({'get': 'list'}), name='api_vacancy_input_change_locks'),
    path('vacancy_input_cleanings/', VacancyInputCleaningViewSet.as_view({'get': 'list'}), name='api_vacancy_input_cleanings'),
    path('vacancy_input_document_prices/', VacancyInputDocumentPriceViewSet.as_view({'get': 'list'}), name='api_vacancy_input_document_prices'),
    path('vacancy_input_electrics/', VacancyInputElectricViewSet.as_view({'get': 'list'}), name='api_vacancy_input_electrics'),
    path('vacancy_input_garages/', VacancyInputGarageViewSet.as_view({'get': 'list'}), name='api_vacancy_input_garages'),
    path('vacancy_input_gases/', VacancyInputGasViewSet.as_view({'get': 'list'}), name='api_vacancy_input_gases'),
    path('vacancy_input_guarantees/', VacancyInputGuaranteeViewSet.as_view({'get': 'list'}), name='api_vacancy_input_guarantees'),
    path('vacancy_input_guarantor_limits/', VacancyInputGuarantorLimitViewSet.as_view({'get': 'list'}), name='api_vacancy_input_guarantor_limits'),
    path('vacancy_input_insurances/', VacancyInputInsuranceViewSet.as_view({'get': 'list'}), name='api_vacancy_input_insurances'),
    path('vacancy_input_internets/', VacancyInputInternetViewSet.as_view({'get': 'list'}), name='api_vacancy_input_internets'),
    path('vacancy_input_payments/', VacancyInputPaymentViewSet.as_view({'get': 'list'}), name='api_vacancy_input_payments'),
    path('vacancy_input_portals/', VacancyInputPortalViewSet.as_view({'get': 'list'}), name='api_vacancy_input_portals'),
    path('vacancy_input_renewal_charges/', VacancyInputRenewalChargeViewSet.as_view({'get': 'list'}), name='api_vacancy_input_renewal_charges'),
    path('vacancy_input_short_cancels/', VacancyInputShortCancelViewSet.as_view({'get': 'list'}), name='api_vacancy_input_short_cancels'),
    path('vacancy_input_waters/', VacancyInputWaterViewSet.as_view({'get': 'list'}), name='api_vacancy_input_waters'),
    path('vacancy_themes/', VacancyThemeViewSet.as_view({'get': 'list'}), name='api_vacancy_themes'),

    path('', TemplateView.as_view(template_name='404.html'), name='api_index'),
]
