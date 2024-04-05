from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_member), # 1. 회원 생성 - 김시원
    path('<int:id>/',views.get_member), # 2. 회원 정보 조회 - 김시원
    path('update_password/<int:id>/',views.update_member_password), # 3. 회원 정보 수정 - 김시원
    path('delete/<int:id>/',views.delete_member), #4. 회원 정보 삭제 - 최우진
    path('add_heart/<int:id>/',views.add_heart_to_member), #5 하트 누르기 - 최우진
    path('appoint/<int:id>/', views.appoint_leader), #6 대표 임명하기 - 손가영
    path('all_list/', views.get_all) #7 모든 회원 정보 조회 - 손가영
]
