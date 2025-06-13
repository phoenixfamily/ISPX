from django.db import models


class About(models.Model):
    company_name = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField()
    logo1 = models.ImageField(upload_to='images/', null=True, blank=True)
    logo2 = models.ImageField(upload_to='images/', null=True, blank=True)
    side_image = models.ImageField(upload_to='images/', null=True, blank=True)
    telegram_id = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()


class Certificate(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
