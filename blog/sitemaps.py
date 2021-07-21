from django.contrib.sitemaps import Sitemap
from .models import blogpost



class Blogpost_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return blogpost.objects.all()