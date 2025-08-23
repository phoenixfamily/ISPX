from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'contact'


urlpatterns = [

    path("", contact_view, name='contact-view'),
    path("api/email/", EmailView.as_view(), name='email-view'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
