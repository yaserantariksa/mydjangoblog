from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            'blog'
        ]
    def location(self, item):
        return reverse(item)
    
class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(is_draft=False)
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, item):
        return item.get_absolute_url()