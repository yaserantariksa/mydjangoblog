from django.contrib import admin
from .models import Tag, Post, Page
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Page)