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


class CooperationRequestView(APIView):
    def post(self, request, *args, **kwargs):
        form = CooperationRequestForm(request.data, request.FILES)
        if form.is_valid():
            ac_type = form.cleaned_data['ac_type']
            date = form.cleaned_data['date']
            ac_reg = form.cleaned_data['ac_reg']
            station = form.cleaned_data.get('station', '')
            time = form.cleaned_data.get('time', '')
            customer = form.cleaned_data.get('customer', '')
            task_cabin = form.cleaned_data['task_cabin']
            task_exterior = form.cleaned_data['task_exterior']

            # Subject and body
            email_subject = f"[Cooperation Request] A/C: {ac_type} - {ac_reg}"
            email_body = (
                f"A/C Type: {ac_type}\n"
                f"Date: {date}\n"
                f"A/C Registration: {ac_reg}\n"
                f"Station: {station}\n"
                f"Time: {time}\n"
                f"Customer: {customer}\n"
                f"Cabin Deep Cleaning: {'Yes' if task_cabin else 'No'}\n"
                f"Exterior Cleaning: {'Yes' if task_exterior else 'No'}\n"
            )

            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email='customer@iranianshiningphoenix.com',  # فرستنده
                to=['ceo@iranianshiningphoenix.com'],  # گیرنده
            )

            # اگر فایلی هم اضافه شد
            file = request.FILES.get('file')
            if file:
                email.attach(file.name, file.read(), file.content_type)

            try:
                email.send()
                return Response({"message": "Cooperation request submitted successfully."}, status=200)
            except Exception as e:
                return Response({"error": f"Error sending email: {str(e)}"}, status=500)
        else:
            return Response({"errors": form.errors}, status=400)