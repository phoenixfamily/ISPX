from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from category.models import Category
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from ISPX.permissions import IsSuperUser



def product_view(request):
    template = loader.get_template('product.html')
    category = Category.objects.all()
    context = {
        'category': category
    }

    return HttpResponse(template.render(context, request))


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories']
    permission_classes = [IsSuperUser]

    @action(detail=False, methods=['DELETE'])
    def delete_all(self, request):
        count, _ = Product.objects.all().delete()
        return Response(f"All {count} product instances were deleted.", status=status.HTTP_204_NO_CONTENT)
