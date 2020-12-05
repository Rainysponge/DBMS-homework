from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('student_consumption', views.student_consumption, name='student_consumption'),
]