"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('input_bike_parking_list/', VacancyInputBikeParkingListView.as_view(), name='vacancy_item_vacancy_input_bike_parking_list'),
    path('input_bike_parking/<str:idb64>', VacancyInputBikeParkingView.as_view(), name='vacancy_item_vacancy_input_bike_parking'),
    path('create_input_bike_parking/', CreateVacancyInputBikeParkingView.as_view(), name='vacancy_item_create_vacancy_input_bike_parking'),

    path('input_cancel_notice_list/', VacancyInputCancelNoticeListView.as_view(), name='vacancy_item_vacancy_input_cancel_notice_list'),
    path('input_cancel_notice/<str:idb64>', VacancyInputCancelNoticeView.as_view(), name='vacancy_item_vacancy_input_cancel_notice'),
    path('create_input_cancel_notice/', CreateVacancyInputCancelNoticeView.as_view(), name='vacancy_item_create_vacancy_input_cancel_notice'),

    path('input_change_lock_list/', VacancyInputChangeLockListView.as_view(), name='vacancy_item_vacancy_input_change_lock_list'),
    path('input_change_lock/<str:idb64>', VacancyInputChangeLockView.as_view(), name='vacancy_item_vacancy_input_change_lock'),
    path('create_input_change_lock/', CreateVacancyInputChangeLockView.as_view(), name='vacancy_item_create_vacancy_input_change_lock'),

    path('input_cleaning_list/', VacancyInputCleaningListView.as_view(), name='vacancy_item_vacancy_input_cleaning_list'),
    path('input_cleaning/<str:idb64>', VacancyInputCleaningView.as_view(), name='vacancy_item_vacancy_input_cleaning'),
    path('create_input_cleaning/', CreateVacancyInputCleaningView.as_view(), name='vacancy_item_create_vacancy_input_cleaning'),

    path('input_document_price_list/', VacancyInputDocumentPriceListView.as_view(), name='vacancy_item_vacancy_input_document_price_list'),
    path('input_document_price/<str:idb64>', VacancyInputDocumentPriceView.as_view(), name='vacancy_item_vacancy_input_document_price'),
    path('create_input_document_price/', CreateVacancyInputDocumentPriceView.as_view(), name='vacancy_item_create_vacancy_input_document_price'),

    path('input_electric_list/', VacancyInputElectricListView.as_view(), name='vacancy_item_vacancy_input_electric_list'),
    path('input_electric/<str:idb64>', VacancyInputElectricView.as_view(), name='vacancy_item_vacancy_input_electric'),
    path('create_input_electric/', CreateVacancyInputElectricView.as_view(), name='vacancy_item_create_vacancy_input_electric'),

    path('input_garage_list/', VacancyInputGarageListView.as_view(), name='vacancy_item_vacancy_input_garage_list'),
    path('input_garage/<str:idb64>', VacancyInputGarageView.as_view(), name='vacancy_item_vacancy_input_garage'),
    path('create_input_garage/', CreateVacancyInputGarageView.as_view(), name='vacancy_item_create_vacancy_input_garage'),

    path('input_gas_list/', VacancyInputGasListView.as_view(), name='vacancy_item_vacancy_input_gas_list'),
    path('input_gas/<str:idb64>', VacancyInputGasView.as_view(), name='vacancy_item_vacancy_input_gas'),
    path('create_input_gas/', CreateVacancyInputGasView.as_view(), name='vacancy_item_create_vacancy_input_gas'),

    path('input_guarantee_list/', VacancyInputGuaranteeListView.as_view(), name='vacancy_item_vacancy_input_guarantee_list'),
    path('input_guarantee/<str:idb64>', VacancyInputGuaranteeView.as_view(), name='vacancy_item_vacancy_input_guarantee'),
    path('create_input_guarantee/', CreateVacancyInputGuaranteeView.as_view(), name='vacancy_item_create_vacancy_input_guarantee'),

    path('input_guarantor_limit_list/', VacancyInputGuarantorLimitListView.as_view(), name='vacancy_item_vacancy_input_guarantor_limit_list'),
    path('input_guarantor_limit/<str:idb64>', VacancyInputGuarantorLimitView.as_view(), name='vacancy_item_vacancy_input_guarantor_limit'),
    path('create_input_guarantor_limit/', CreateVacancyInputGuarantorLimitView.as_view(), name='vacancy_item_create_vacancy_input_guarantor_limit'),

    path('input_insurance_list/', VacancyInputInsuranceListView.as_view(), name='vacancy_item_vacancy_input_insurance_list'),
    path('input_insurance/<str:idb64>', VacancyInputInsuranceView.as_view(), name='vacancy_item_vacancy_input_insurance'),
    path('create_input_insurance/', CreateVacancyInputInsuranceView.as_view(), name='vacancy_item_create_vacancy_input_insurance'),

    path('input_internet_list/', VacancyInputInternetListView.as_view(), name='vacancy_item_vacancy_input_internet_list'),
    path('input_internet/<str:idb64>', VacancyInputInternetView.as_view(), name='vacancy_item_vacancy_input_internet'),
    path('create_input_internet/', CreateVacancyInputInternetView.as_view(), name='vacancy_item_create_vacancy_input_internet'),

    path('input_payment_list/', VacancyInputPaymentListView.as_view(), name='vacancy_item_vacancy_input_payment_list'),
    path('input_payment/<str:idb64>', VacancyInputPaymentView.as_view(), name='vacancy_item_vacancy_input_payment'),
    path('create_input_payment/', CreateVacancyInputPaymentView.as_view(), name='vacancy_item_create_vacancy_input_payment'),

    path('input_portal_list/', VacancyInputPortalListView.as_view(), name='vacancy_item_vacancy_input_portal_list'),
    path('input_portal/<str:idb64>', VacancyInputPortalView.as_view(), name='vacancy_item_vacancy_input_portal'),
    path('create_input_portal/', CreateVacancyInputPortalView.as_view(), name='vacancy_item_create_vacancy_input_portal'),

    path('input_renewal_charge_list/', VacancyInputRenewalChargeListView.as_view(), name='vacancy_item_vacancy_input_renewal_charge_list'),
    path('input_renewal_charge/<str:idb64>', VacancyInputRenewalChargeView.as_view(), name='vacancy_item_vacancy_input_renewal_charge'),
    path('create_input_renewal_charge/', CreateVacancyInputRenewalChargeView.as_view(), name='vacancy_item_create_vacancy_input_renewal_charge'),

    path('input_short_cancel_list/', VacancyInputShortCancelListView.as_view(), name='vacancy_item_vacancy_input_short_cancel_list'),
    path('input_short_cancel/<str:idb64>', VacancyInputShortCancelView.as_view(), name='vacancy_item_vacancy_input_short_cancel'),
    path('create_input_short_cancel/', CreateVacancyInputShortCancelView.as_view(), name='vacancy_item_create_vacancy_input_short_cancel'),

    path('input_water_list/', VacancyInputWaterListView.as_view(), name='vacancy_item_vacancy_input_water_list'),
    path('input_water/<str:idb64>', VacancyInputWaterView.as_view(), name='vacancy_item_vacancy_input_water'),
    path('create_input_water/', CreateVacancyInputWaterView.as_view(), name='vacancy_item_create_vacancy_input_water'),

    path('theme_list/', VacancyThemeListView.as_view(), name='vacancy_item_vacancy_theme_list'),
    path('theme/<str:idb64>', VacancyThemeView.as_view(), name='vacancy_item_vacancy_theme'),
    path('create_theme/', CreateVacancyThemeView.as_view(), name='vacancy_item_create_vacancy_theme'),

    path('', TemplateView.as_view(template_name='404.html'), name='vacancy_item_index'),
]
