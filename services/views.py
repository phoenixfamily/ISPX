from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from category.models import Category
from .models import Services
from .serializers import ServicesSerializer
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from ISPX.permissions import IsSuperUser


def services_view(request, pk):
    template = loader.get_template('services.html')
    category = Category.objects.all()
    services = Services.objects.filter(categories=pk)
    context = {
        'category': category,
        'services': services
    }
    return HttpResponse(template.render(context, request))


def update_services_view(request, pk):
    template = loader.get_template('update-services.html')
    service = get_object_or_404(Services, pk=pk)
    context = {
        'service': service
    }
    return HttpResponse(template.render(context, request))


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsSuperUser]
