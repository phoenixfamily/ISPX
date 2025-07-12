# sitemap.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Services

class ServiceSitemap(Sitemap):
    changefreq = "daily"  # بسته به به‌روزرسانی سایت، می‌تونی تنظیمش کنی
    priority = 0.9  # اهمیت صفحه برای گوگل
    protocol = 'https'  # اگر سایتت SSL داره

    def items(self):
        return Services.objects.all()  # فقط محصولات فعال رو بگیر

    def location(self, item):
        return reverse('services:services-view', args=[item.id])  # اگه از ID استفاده می‌کنی