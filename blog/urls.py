from django.urls import path
from .views import index, post

urlpatterns = [
    path('', index, name='blog'),
    path('<slug:slug>/', post)
]
