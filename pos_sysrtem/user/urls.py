from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('changestudentinfo/<int:user_pk>', views.changeStudentInfo, name='changestudentinfo'),
    path('changeteacherinfo/<int:user_pk>', views.changeTeacherInfo, name='changeteacherinfo'),
    path('changeshopownerinfo/<int:user_pk>', views.changeShopownerInfo, name='changeshopownerinfo'),
]
