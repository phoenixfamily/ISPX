from django.db import models
from category.models import Category


# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    categories = models.ForeignKey(Category, related_name='services', on_delete=models.CASCADE, null=True , blank=True)
