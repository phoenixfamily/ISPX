from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page

from category.models import Category
from .models import Services
from .serializers import ServicesSerializer
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from ISPX.permissions import IsSuperUser


@cache_page(60 * 15)
def services_view(request, pk):
    template = loader.get_template('services.html')
    category = Category.objects.all()
    services = Services.objects.filter(categories=pk)
    context = {
        'category': category,
        'services': services
    }
    return HttpResponse(template.render(context, request))


class ServicesCreateView(generics.CreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsSuperUser]


class ServicesDetailView(viewsets.ViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsSuperUser]

    def destroy(self, request, pk):
        try:
            services = Services.objects.get(pk=pk)
            services.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Services.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        try:
            services = Services.objects.get(pk=pk)
        except Services.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(services, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
