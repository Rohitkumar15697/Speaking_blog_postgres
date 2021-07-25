from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import blogpost



class BlogpostSitemap(Sitemap):
    changefreq='never'
    priority=0.9
    def items(self):
        return blogpost.objects.all()

    def lastmod(self, obj):
        return obj.date