from django.urls import path
from . import views

urlpatterns = [
    path('submit-resume/', views.submit_resume, name='submit_resume'),
    path('resume-success/', views.resume_success, name='resume_success'),
    path('', views.index, name="home"),
    path('resume/<int:resume_id>/edit/', views.edit_resume, name='edit_resume'),
]