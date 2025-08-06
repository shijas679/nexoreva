from django.urls import path
from . import views

urlpatterns = [
    path('assignment-user-list/', views.viewwork_assignment_userlist_staff, name='viewwork_assignment_userlist_staff'),
    path('add-assignment/', views.add_assignment_view, name='add_assignment_view'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/add/', views.add_assignment_view, name='add_assignment'),
    path('add-assignment/<int:user_id>/', views.add_assignment_view, name='add_assignment_view'),
    path('assignment/<int:assignment_id>/edit/', views.edit_assignment, name='edit_assignment'),
    path('assignment/<int:assignment_id>/delete/', views.delete_assignment, name='delete_assignment'),
]