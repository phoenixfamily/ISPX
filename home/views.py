from django.core.mail import EmailMessage
from django.http import HttpResponse
from rest_framework.views import APIView

from category.models import Category
from .forms import CooperationRequestForm
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


from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .forms import CooperationRequestForm

def cooperation_request_view(request):
    if request.method == 'POST':
        form = CooperationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            # ایمیل ساختن و ارسال همونطوری که قبلاً گفتیم
            email_subject = "New Cooperation Request"
            email_body = "\n".join([f"{field.label}: {form.cleaned_data.get(field.name)}" for field in form])

            email = EmailMessage(
                email_subject,
                email_body,
                'customer@iranianshiningphoenix.com',
                ['ceo@iranianshiningphoenix.com'],
            )
            email.send()

            return HttpResponse("Success")
        else:
            return HttpResponse("Invalid form", status=400)

    else:
        form = CooperationRequestForm()
    return render(request, 'cooperation_form.html', {'form': form})
.errors}, status=400)