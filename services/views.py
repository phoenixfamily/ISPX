from django.http import HttpResponse
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


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsSuperUser]