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
