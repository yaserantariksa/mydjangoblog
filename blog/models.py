import datetime
from django.db import models
from django.utils.text import slugify
from django_quill.fields import QuillField

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(primary_key=True, unique=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    content = QuillField()
    image = models.ImageField(upload_to="upload/", blank=True, null=True)
    video= models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(Tag,blank=True)
    is_draft = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    
class Page(models.Model):
    title = models.CharField(max_length=70)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

