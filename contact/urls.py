from django.conf.urls.static import static
from django.urls import path

from ISPX import settings
from .views import *


app_name = 'contact'

urlpatterns = [

    path("", contact_view, name='view'),
    path('api/', EmailView.as_view(), name='email'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
