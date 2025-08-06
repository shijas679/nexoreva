from django.urls import path
from .views import add_staff, view_staff, edit_staff, delete_staff

urlpatterns = [
    path('add/', add_staff, name='add_staff'),
    path('view/', view_staff, name='view_staff'),
<<<<<<< HEAD
    
]
=======
    path('edit/<int:staff_id>/', edit_staff, name='edit_staff'),
    path('delete/<int:staff_id>/', delete_staff, name='delete_staff'),
]

>>>>>>> f5cf8ae058cc2e7ce1a8dfe72ade2f7808dec3c4
