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

from django.contrib import admin
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from homeapp import sitemaps
from homeapp.sitemaps import BlogpostSitemap
from django.views.generic import TemplateView   #This is for robots.txt

sitemaps={'blogpost':BlogpostSitemap}



urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('',include('homeapp.urls')), 
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('robots.txt',TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
    path('account/',include('account.urls')),
    path('blog/',include('blog.urls')),
    
]

#For accessing media files on admin pannel like open image in full size after clicking on it

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)