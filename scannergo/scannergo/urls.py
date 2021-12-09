"""scannergo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from scannergoapp import views
#from scannergoapp.views import DisplayView
from scannergoapp.views import midView
from scannergoapp.views import PicSubmissionView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from scannergo.settings import SITE_ROOT
import os
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PicSubmissionView.as_view(), name='null'),
    path('home/', PicSubmissionView.as_view(), name='first'),
    path('delete/', views.delete, name='del'),
    path('run/', views.getoutput, name='run'),
    path('display/', views.index, name='pic-submission-null'),
    path('home/display/', views.index, name='pic-submission'),
    path('connect/', midView.as_view(), name='mid-null'),
    path('home/connect/', midView.as_view(), name='mid'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#else:
#    urlpatterns += staticfiles_urlpatterns()
