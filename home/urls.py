from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


app_name = 'home'

router = DefaultRouter()
router.register(r'slider', SliderViewSet)
router.register(r'CEO', CeoViewSet)



urlpatterns = [
    path("", home_view, name='home-view'),
    path("api/", include(router.urls)),
    path("api/cooperation/", CooperationRequestViewSet.as_view({'post': 'create'}), name="cooperation"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
