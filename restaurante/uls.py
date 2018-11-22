from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include

urlpatterns = [
    path('plato/nuevo/', views.nuevo_plato, name='nuevo_plato'),
]
