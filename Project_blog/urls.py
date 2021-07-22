"""Project_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from blog.models import blogpost
from django.contrib import admin
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from blog import sitemaps
from blog.sitemaps import BlogpostSitemap

sitemaps={'blogpost':BlogpostSitemap}



urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('',include('homeapp.urls')), 
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('account/',include('account.urls')),
    path('blog/',include('blog.urls')),
]
