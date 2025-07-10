"""
URL configuration for IranianShiningPhoenix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.i18n import set_language
from rest_framework.authtoken.views import obtain_auth_token
from about.views import *
from contact.views import *
from products.views import *
from services.views import *
from category.views import *
from home.views import *
from ISPX import settings


urlpatterns = [

    path('', RedirectView.as_view(url='/home/', permanent=True)),

    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),  # مسیر پنل ادمین
    path('set_language/', set_language, name='set_language'),  # به جای include از set_language استفاده کنید
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

]

urlpatterns += i18n_patterns(
    path('about/', include('about.urls', namespace='about')),  # مسیر URLهای اپلیکیشن About
    path('category/', include('category.urls', namespace='category')),  # مسیر URLهای اپلیکیشن Blog
    path('contact/', include('contact.urls', namespace='contact')),  # مسیر URLهای اپلیکیشن Contact
    path('home/', include('home.urls', namespace='home')),  # مسیر URLهای اپلیکیشن Home
    path('services/', include('services.urls', namespace='services')),  # مسیر URLهای اپلیکیشن Services
    path('products/', include('products.urls', namespace='products')),  # مسیر URLهای اپلیکیشن Product
    path('auth/', include('services.urls', namespace='services')),  # مسیر URLهای اپلیکیشن Authentication

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
