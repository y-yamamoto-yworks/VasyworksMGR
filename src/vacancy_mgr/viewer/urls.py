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
    path('private_media/<path:file_url>', PrivateMediaViewerView.as_view(), name='viewer_private_media'),
    path('public_media/<path:file_url>', PublicMediaViewerView.as_view(), name='viewer_public_media'),

    path('', TemplateView.as_view(template_name='404.html'), name='viewer_index'),
]
