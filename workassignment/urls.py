from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='workassignment_home'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/add/', views.add_assignment, name='add_assignment'),
]
