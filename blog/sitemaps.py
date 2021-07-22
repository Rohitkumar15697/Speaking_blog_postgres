import homeapp
from django.contrib.sitemaps import Sitemap
from .models import blogpost

class BlogpostSitemap(Sitemap):
    def items(self):
        return blogpost.objects.all()