from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resume/<int:resume_id>/', views.resume_detail, name='resume_detail'),
    path('resume/<int:resume_id>/generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('', views.index, name="index"),
    path('resume_qr/<int:resume_id>/', views.generate_resume_qr, name='resume_qr'),
    path('error/', views.errorpage, name="404"),
    path('system-register/', views.sysregister, name="system_register"),
    path('sys-content/', views.content, name="content"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)