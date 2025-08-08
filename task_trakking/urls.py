from django.urls import path 
from . import views

urlpatterns = [
    path('task-status/', views.task_status, name='task-status'),
    path('update_status/<staff_id>',views.update_status, name='update_status')
]