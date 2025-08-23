from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'seo', views.SEOPageView, basename='seo')
router.register(r'keyword', views.KeywordView, basename='keyword')

app_name = 'seo'

urlpatterns = [
    path('api/', include(router.urls)),
]
