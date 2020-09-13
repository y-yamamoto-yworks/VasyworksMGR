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
    path('user_list/', UserListView.as_view(), name='users_user_list'),
    path('user_list/all/', UserListView.as_view(all_users=True), name='users_all_user_list'),
    path('user/<str:idb64>', UserView.as_view(), name='users_user'),
    path('user/change_password/<str:idb64>', ChangeUserPasswordView.as_view(), name='users_user_change_password'),
    path('user/create_user/', CreateUserView.as_view(), name='users_create_user'),
    path('user/create_user/<str:staff_idb64>', CreateUserView.as_view(), name='users_create_user'),

    path('vacancy_user_list/', VacancyUserListView.as_view(), name='users_vacancy_user_list'),
    path('vacancy_user_list/all/', VacancyUserListView.as_view(all_users=True), name='users_all_vacancy_user_list'),
    path('vacancy_user/<str:idb64>', VacancyUserView.as_view(), name='users_vacancy_user'),
    path('vacancy_user/change_password/<str:idb64>', ChangeVacancyUserPasswordView.as_view(), name='users_vacancy_user_change_password'),
    path('user/create_vacancy_user/', CreateVacancyUserView.as_view(), name='users_create_vacancy_user'),

    path('', TemplateView.as_view(template_name='404.html'), name='users_index'),
]
