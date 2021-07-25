from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import blogpost

class StaticPages(Sitemap):
    changefreq='daily'
    priority=0.5
    def items(self):
        return ['home','about']
    def location(self, item):
        return reverse(item)

class BlogpostSitemap(Sitemap):
    changefreq='never'
    priority=0.9
    def items(self):
        return blogpost.objects.all()

    def lastmod(self, obj):
        return obj.date