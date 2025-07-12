from django.db import models

# Create your models here.
# models.py
class SEOFields(models.Model):
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    canonical_url = models.URLField(blank=True, null=True)
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True)
    # می‌تونی به هر مدل اصلی وصلش کنی با OneToOneField
