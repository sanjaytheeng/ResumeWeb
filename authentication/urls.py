from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('reset-password', views.reset_password, name='reset_password'),
]