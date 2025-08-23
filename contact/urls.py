from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'contact'


urlpatterns = [

    path("", contact_view, name='contact-view'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
