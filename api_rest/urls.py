from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_users_by_nick)
]