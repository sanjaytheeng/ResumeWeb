from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('resume/<int:resume_id>/', views.resume_detail, name='resume_detail'),
    #  path('resume/<int:resume_id>/generate_pdf/', generate_pdf, name='generate_pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)