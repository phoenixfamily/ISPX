# ISPX/urls.py
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from django.views.i18n import set_language

from seo.sitemaps import StaticViewSitemap
from services.sitemaps import ServiceSitemap
from ISPX import settings

# اگر flatpages استفاده نمی‌کنی، ایمپورت ماژول sitemaps از flatpages رو حذف کن

sitemaps_dict = {   # اسم دیکشنری رو عوض کردیم
    'static': StaticViewSitemap(),
    'services': ServiceSitemap(),
}

urlpatterns = [
    # ریدایرکت ریشه به نام URL صفحه خانه (فرض: در home.urls نام 'home:index' داری)
    path('', RedirectView.as_view(url=reverse_lazy('home:index'), permanent=True), name='root'),

    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    # تغییر زبان (POST)
    path('set_language/', set_language, name='set_language'),

    # سایت‌مپ
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),

]

urlpatterns += i18n_patterns(
    path('home/', include(('home.urls', 'home'), namespace='home')),
    path('about/', include(('about.urls', 'about'), namespace='about')),
    path('category/', include(('category.urls', 'category'), namespace='category')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('services/', include(('services.urls', 'services'), namespace='services')),
    path('products/', include(('products.urls', 'products'), namespace='products')),
    # اگر auth داری:
    # path('auth/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    prefix_default_language=False,  # پیشنهاد: زبان پیش‌فرض بدون پیشوند
)

# فقط در DEBUG:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
