from django.db import models
from django.utils import timezone


# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    # datetime = models.DateTimeField(default=timezone.now)


class CEO(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField()




class CooperationRequest(models.Model):
    AC_TYPE_CHOICES = [
        ('narrow', 'Narrow Body'),
        ('wide', 'Wide Body'),
        # اگر خواستی انتخابی‌ش کن
    ]

    ac_type = models.CharField("A/C Type", max_length=100)
    date = models.DateField("Date")
    ac_reg = models.CharField("A/C Registration", max_length=50)
    station = models.CharField("Station", max_length=100, blank=True, null=True)
    time = models.TimeField("Time", blank=True, null=True)
    customer = models.CharField("Customer", max_length=100, blank=True, null=True)

    task_cabin = models.BooleanField("Cabin Deep Cleaning", default=False)
    task_exterior = models.BooleanField("Exterior Cleaning", default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request {self.ac_type} - {self.date}"
