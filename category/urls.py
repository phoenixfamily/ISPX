from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'category-view', CategoryViewSet)
# category bulk delete: http://127.0.0.1:8000/category/category-view/delete_all/

app_name = 'category'


urlpatterns = [
    path("api/", include(router.urls)),
]
