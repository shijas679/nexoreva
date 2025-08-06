from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_home, name='attendance_home'),
    path('time_in/', views.time_in, name='time_in'),
    path('time_out/', views.time_out, name='time_out'),
    path('records/', views.records, name='attendance_records'),

]
