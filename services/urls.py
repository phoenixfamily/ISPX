from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter
from ISPX import settings
from .views import *

app_name = 'services'

router = DefaultRouter()
router.register(r'api/services', ServicesViewSet, basename='services')

urlpatterns = [
                  path("<int:pk>/", services_view, name='services_view'),
                  path("<int:pk>/", uodate_services_view, name='update_services_view'),

              ] + router.urls

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
