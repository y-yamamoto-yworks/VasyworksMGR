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
    path('edit_document_file/<str:idb64>', EditDocumentFileView.as_view(), name='documents_edit_document_file'),
    path('delete_document_file/<str:idb64>', DeleteDocumentFileView.as_view(), name='documents_delete_document_file'),
    path('upload_document_file/', UploadDocumentFileView.as_view(), name='documents_upload_document_file'),

    path('', DocumentFileListView.as_view(), name='documents_index'),
]
