from django.contrib.sitemaps import Sitemap
from blog.models import blogpost



class Blogpost_Sitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    def items(self):
        return blogpost.objects.all()