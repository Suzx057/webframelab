from django.urls import path
from .views import add_video, add_author, list_videos, list_authors

urlpatterns = [
    path('add_video/', add_video, name='add_video'),
    path('add_author/', add_author, name='add_author'),
    path('list_videos/', list_videos, name='list_videos'),
    path('list_authors/', list_authors, name='list_authors'),
]