from django.urls import path
from .views import dashboard_view, user_login

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', user_login, name='login'),
]
