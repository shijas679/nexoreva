from django.urls import path
from . import views
from dashboard.views import user_login  # Import your dashboard login view

urlpatterns = [
    path('', views.attendance_home, name='attendance_home'),
    path('attendance_action/', views.attendance_action, name='attendance_action'),
    path('leave/', views.leave_request, name='leave_request'),
    path('login/', user_login, name='login'),  # Points to your dashboard's login view
    path('attendence_details/', views.attendance_details, name='attendence_details'),
    path('leave-details/<int:staff_id>/', views.leave_details, name='leave_details'),  # NEW: Leave details view
]
