"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from django.views.generic import TemplateView
from property.views import *

urlpatterns = [
    path('building/<str:oid>', BuildingView.as_view(), name='property_building'),
    path('building/edit/<str:oid>', EditBuildingView.as_view(), name='property_edit_building'),
    path('building/edit_latlng/<str:oid>', EditBuildingLatLngView.as_view(), name='property_edit_building_latlng'),
    path('building/create/', CreateBuildingView.as_view(), name='property_create_building'),
    path('building/delete/<str:oid>', DeleteBuildingView.as_view(), name='property_delete_building'),

    path('building/create_building_facility/<str:building_oid>', CreateBuildingFacilityView.as_view(), name='property_create_building_facility'),
    path('building/edit_building_facility/<str:building_oid>/<int:id>', EditBuildingFacilityView.as_view(), name='property_edit_building_facility'),
    path('building/delete_building_facility/<str:building_oid>/<int:id>', DeleteBuildingFacilityView.as_view(), name='property_delete_building_facility'),

    path('building/create_building_garage/<str:building_oid>', CreateBuildingGarageView.as_view(), name='property_create_building_garage'),
    path('building/edit_building_garage/<str:building_oid>/<int:id>', EditBuildingGarageView.as_view(), name='property_edit_building_garage'),
    path('building/delete_building_garage/<str:building_oid>/<int:id>', DeleteBuildingGarageView.as_view(), name='property_delete_building_garage'),

    path('building/create_building_landmark/<str:building_oid>', CreateBuildingLandmarkView.as_view(), name='property_create_building_landmark'),
    path('building/edit_building_landmark/<str:building_oid>/<int:id>', EditBuildingLandmarkView.as_view(), name='property_edit_building_landmark'),
    path('building/delete_building_landmark/<str:building_oid>/<int:id>', DeleteBuildingLandmarkView.as_view(), name='property_delete_building_landmark'),

    path('building/upload_building_file/<str:building_oid>', UploadBuildingFileView.as_view(), name='property_upload_building_file'),
    path('building/edit_building_file/<str:building_oid>/<int:id>', EditBuildingFileView.as_view(), name='property_edit_building_file'),
    path('building/delete_building_file/<str:building_oid>/<int:id>', DeleteBuildingFileView.as_view(), name='property_delete_building_file'),

    path('building/upload_building_movie/<str:building_oid>', UploadBuildingMovieView.as_view(), name='property_upload_building_movie'),
    path('building/edit_building_movie/<str:building_oid>/<int:id>', EditBuildingMovieView.as_view(), name='property_edit_building_movie'),
    path('building/delete_building_movie/<str:building_oid>/<int:id>', DeleteBuildingMovieView.as_view(), name='property_delete_building_movie'),

    path('building/upload_building_panorama/<str:building_oid>', UploadBuildingPanoramaView.as_view(), name='property_upload_building_panorama'),
    path('building/edit_building_panorama/<str:building_oid>/<int:id>', EditBuildingPanoramaView.as_view(), name='property_edit_building_panorama'),
    path('building/delete_building_panorama/<str:building_oid>/<int:id>', DeleteBuildingPanoramaView.as_view(), name='property_delete_building_panorama'),

    path('building/upload_building_picture/<str:building_oid>', UploadBuildingPictureView.as_view(), name='property_upload_building_picture'),
    path('building/edit_building_picture/<str:building_oid>/<int:id>', EditBuildingPictureView.as_view(), name='property_edit_building_picture'),
    path('building/delete_building_picture/<str:building_oid>/<int:id>', DeleteBuildingPictureView.as_view(), name='property_delete_building_picture'),

    path('room/<str:oid>', RoomView.as_view(), name='property_room'),
    path('room/edit/<str:oid>', EditRoomView.as_view(), name='property_edit_room'),
    path('room/copy/<str:oid>', CopyRoomDataView.as_view(), name='property_copy_room'),
    path('room/create/<str:building_oid>', CreateRoomView.as_view(), name='property_create_room'),
    path('room/delete/<str:oid>', DeleteRoomView.as_view(), name='property_delete_room'),

    path('room/create_room_equipment/<str:room_oid>', CreateRoomEquipmentView.as_view(), name='property_create_room_equipment'),
    path('room/edit_room_equipment/<str:room_oid>/<int:id>', EditRoomEquipmentView.as_view(), name='property_edit_room_equipment'),
    path('room/delete_room_equipment/<str:room_oid>/<int:id>', DeleteRoomEquipmentView.as_view(), name='property_delete_room_equipment'),
    path('room/copy_room_equipment/<str:room_oid>', CopyRoomEquipmentView.as_view(), name='property_copy_room_equipment'),

    path('room/upload_room_movie/<str:room_oid>', UploadRoomMovieView.as_view(), name='property_upload_room_movie'),
    path('room/edit_room_movie/<str:room_oid>/<int:id>', EditRoomMovieView.as_view(), name='property_edit_room_movie'),
    path('room/delete_room_movie/<str:room_oid>/<int:id>', DeleteRoomMovieView.as_view(), name='property_delete_room_movie'),

    path('room/upload_room_panorama/<str:room_oid>', UploadRoomPanoramaView.as_view(), name='property_upload_room_panorama'),
    path('room/edit_room_panorama/<str:room_oid>/<int:id>', EditRoomPanoramaView.as_view(), name='property_edit_room_panorama'),
    path('room/delete_room_panorama/<str:room_oid>/<int:id>', DeleteRoomPanoramaView.as_view(), name='property_delete_room_panorama'),

    path('room/upload_room_picture/<str:room_oid>', UploadRoomPictureView.as_view(), name='property_upload_room_picture'),
    path('room/edit_room_picture/<str:room_oid>/<int:id>', EditRoomPictureView.as_view(), name='property_edit_room_picture'),
    path('room/delete_room_picture/<str:room_oid>/<int:id>', DeleteRoomPictureView.as_view(), name='property_delete_room_picture'),
    path('room/copy_room_picture/<str:room_oid>', CopyRoomPictureView.as_view(), name='property_copy_room_picture'),

    path('room/create_room_vacancy_theme/<str:room_oid>', CreateRoomVacancyThemeView.as_view(), name='property_create_room_vacancy_theme'),
    path('room/delete_room_vacancy_theme/<str:room_oid>/<int:id>', DeleteRoomVacancyThemeView.as_view(), name='property_delete_room_vacancy_theme'),

    path('', TemplateView.as_view(template_name='404.html'), name='property_index'),
]
