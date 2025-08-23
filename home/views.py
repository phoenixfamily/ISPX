from django.core.mail import EmailMessage
from django.http import HttpResponse
from rest_framework.views import APIView

from category.models import Category
from .forms import CooperationForm
from .models import Slider, CEO, CooperationRequest
from .serializers import SliderSerializer, CeoSerializer, CooperationRequestSerializer
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


class CeoViewSet(viewsets.ModelViewSet):
    queryset = CEO.objects.all()
    serializer_class = CeoSerializer
    permission_classes = [IsSuperUser]

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        count, _ = Slider.objects.all().delete()
        return Response(f"All {count} Services instances were deleted.", status=status.HTTP_204_NO_CONTENT)


class CooperationView(APIView):
    def post(self, request, *args, **kwargs):
        form = CooperationForm(request.data)
        if form.is_valid():
            ac_type = form.cleaned_data["ac_type"]
            date = form.cleaned_data["date"]
            ac_reg = form.cleaned_data["ac_reg"]
            station = form.cleaned_data.get("station") or "-"
            time = form.cleaned_data.get("time")
            customer = form.cleaned_data.get("customer") or "-"

            # چک‌باکس‌ها: اگر "on" باشند True
            task_cabin = bool(request.data.get("task_cabin") == "on")
            task_exterior = bool(request.data.get("task_exterior") == "on")

            subject = f"Cooperation Request - {ac_type} / {ac_reg} / {date}"
            body_lines = [
                f"A/C TYPE: {ac_type}",
                f"DATE: {date}",
                f"A/C REG: {ac_reg}",
                f"STATION: {station}",
                f"TIME: {time if time else '-'}",
                f"CUSTOMER: {customer}",
                "",
                "TASK REQUESTED:",
                f"- CABIN DEEP CLEANING: {'Yes' if task_cabin else 'No'}",
                f"- EXTERIOR CLEANING: {'Yes' if task_exterior else 'No'}",
            ]
            body = "\n".join(body_lines)

            msg = EmailMessage(
                subject=subject,
                body=body,
                from_email="customer@iranianshiningphoenix.ir",  # از سرور خودت
                to=["ceo@iranianshiningphoenix.ir"],  # گیرنده
            )

            try:
                msg.send()
                return Response({"message": "Email sent"}, status=200)
            except Exception as e:
                return Response({"error": f"SMTP error: {e}"}, status=500)

        return Response({"error": form.errors}, status=400)
