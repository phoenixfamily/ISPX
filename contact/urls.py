from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'contact'

router = DefaultRouter()
router.register(r'contact', ContactFormViewSet)

urlpatterns = [

    path("", contact_view, name='view'),
    path("api/", include(router.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
