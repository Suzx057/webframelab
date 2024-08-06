# authors/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('formset/', views.author_formset_view, name='author_formset'),
    path('list/', views.author_list_view, name='author_list'),
    path('videos/', views.author_video_view, name='author_video'),
]