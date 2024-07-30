from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Video, Course

class ShowVideo(View):
    def get(self, request, video_title):
        videos = Video.objects.filter(title=video_title)
        if videos.count() == 1:
            video = videos.first()
            return render(request, 'videos/showvideo.html', {'video': video})
        elif videos.count() > 1:
            return render(request, 'videos/showvideos.html', {'videos': videos})
        else:
            return render(request, 'videos/showvideos.html', {'videos': []})

class ShowCourseVideo(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        videos = course.videos.all()
        return render(request, 'videos/showcoursevideo.html', {'course': course, 'videos': videos})