from django.urls import path
from .views import ShowVideo, ShowCourseVideo

urlpatterns = [
    path('showvideo/<str:video_title>/', ShowVideo.as_view(), name='showvideo'),
    path('showcoursevideo/<int:course_id>/', ShowCourseVideo.as_view(), name='showcourse'),
]