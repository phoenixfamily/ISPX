from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"  # بسته به به‌روزرسانی سایت، می‌تونی تنظیمش کنی
    protocol = 'https'  # اگر سایتت SSL داره


    def items(self):
        return [
            'home:home-view',
            'about:about-view',
            'contact:contact-view',
            'products:product-view',
        ]

    def location(self, item):
        return reverse(item)
