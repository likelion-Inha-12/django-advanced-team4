from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_member), # 1. 회원 생성 - 김시원
    path('<int:id>/',views.get_member), # 2. 회원 정보 조회 - 김시원
    path('update_password/<int:id>/',views.update_member_password), # 3. 회원 정보 수정 - 김시원
]