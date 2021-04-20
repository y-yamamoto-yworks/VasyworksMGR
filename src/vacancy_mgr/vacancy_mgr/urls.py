"""vacancy_mgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
import os
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LogoutView
from users.views import LoginView
from menu.views import MenuIndexView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('api/', include('api.urls')),
    path('property/', include('property.urls')),
    path('company/', include('company.urls')),
    path('documents/', include('documents.urls')),
    path('enums/', include('enums.urls')),
    path('info/', include('info.urls')),
    path('masters/', include('masters.urls')),
    path('menu/', include('menu.urls')),
    path('owner/', include('owner.urls')),
    path('search/', include('search.urls')),
    path('trader/', include('trader.urls')),
    path('users/', include('users.urls')),
    path('vacancy_item/', include('vacancy_item.urls')),
    path('viewer/', include('viewer.urls')),

    path('', MenuIndexView.as_view(), name='top'),
]

urlpatterns += static(settings.MEDIA_URL + 'public/', document_root=os.path.join(settings.MEDIA_ROOT, 'public'))
