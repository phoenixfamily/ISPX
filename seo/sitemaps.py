from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home:view', 'about:view', 'contact:view', 'product:view']

    def location(self, item):
        return reverse(item)
a