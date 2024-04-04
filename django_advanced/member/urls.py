from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_member),
    path('<int:id>/',views.get_member),
    path('update_password/<int:id>/',views.update_member_password),
]