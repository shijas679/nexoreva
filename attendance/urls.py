# attendance/urls.py
from django.urls import path
from . import views
from dashboard.views import user_login   # import your dashboard login view

urlpatterns = [
    path('', views.attendance_home, name='attendance_home'),
    path('attendance_action/', views.attendance_action, name='attendance_action'),
    path('leave/', views.leave_request, name='leave_request'),
    # path('add_task/', views.add_task, name='add_task'),
    path('login/', user_login, name='login'),  # Points to your dashboard's login view
]
