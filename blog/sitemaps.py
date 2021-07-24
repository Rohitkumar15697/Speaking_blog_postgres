import homeapp
from django.contrib.sitemaps import Sitemap
from .models import blogpost

class BlogpostSitemap(Sitemap):
    changefreq='never'
    priority=0.9
    def items(self):
        return blogpost.objects.all()

    def lastmod(self, obj):
        return obj.date