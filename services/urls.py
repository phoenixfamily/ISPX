from django.conf.urls.static import static
from django.urls import path

from ISPX import settings
from .views import *


app_name = 'services'

urlpatterns = [
    path('api/service/', ServicesCreateView.as_view(), name='create-service'),
    path('api/service/update/<int:pk>/', ServicesDetailView.as_view({'put': 'update'}), name='update-service'),
    path('api/service/delete/<int:pk>/', ServicesDetailView.as_view({'delete': 'destroy'}), name='delete-service'),
    path("<int:pk>/", services_view, name='services_view'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
