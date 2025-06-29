from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from rest_framework import generics

from category.models import Category
from .models import Slider, CEO
from .serializers import SliderSerializer, CeoSerializer
from django.template import loader
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from ISPX.permissions import IsSuperUser


def home_view(request):
    template = loader.get_template('home.html')
    category = Category.objects.all()
    context = {
        'category': category
    }
    return HttpResponse(template.render(context, request))


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsSuperUser]

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        count, _ = Slider.objects.all().delete()
        return Response(f"All {count} Services instances were deleted.", status=status.HTTP_204_NO_CONTENT)


# class SliderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Slider.objects.all()
#     serializer_class = SliderSerializer
#
#
# class SliderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Slider.objects.all()
#     serializer_class = SliderSerializer

class CeoViewSet(viewsets.ModelViewSet):
    queryset = CEO.objects.all()
    serializer_class = CeoSerializer
    permission_classes = [IsSuperUser]

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        count, _ = Slider.objects.all().delete()
        return Response(f"All {count} Services instances were deleted.", status=status.HTTP_204_NO_CONTENT)

# class CeoListCreateAPIView(generics.ListCreateAPIView):
#     queryset = CEO.objects.all()
#     serializer_class = CeoSerializer
#
#
# class CeoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CEO.objects.all()
#     serializer_class = CeoSerializer
