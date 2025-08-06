# staff/urls.py

from django.urls import path
from .views import add_staff, view_staff

urlpatterns = [
    path('add/', add_staff, name='add_staff'),
    path('view/', view_staff, name='view_staff'),
]
