# staff/urls.py

from django.urls import path
from .views import add_staff, view_staff, edit_staff, delete_staff
from .views import search_staff_by_code

urlpatterns = [
    path('add/', add_staff, name='add_staff'),
    path('view/', view_staff, name='view_staff'),
    path('edit/<int:staff_id>/', edit_staff, name='edit_staff'),
    path('delete/<int:staff_id>/', delete_staff, name='delete_staff'),
    path('search_code/', search_staff_by_code, name='search_staff_code'),
    path('search-staff/', search_staff_by_code, name='search_staff_by_code'),

]
