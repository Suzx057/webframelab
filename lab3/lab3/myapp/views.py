from django.shortcuts import render, redirect
from .forms import VideoForm, AuthorForm
from .models import Video, Author

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_videos')
    else:
        form = VideoForm()
    return render(request, 'myapp/add_video.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_authors')
    else:
        form = AuthorForm()
    return render(request, 'myapp/add_author.html', {'form': form})

def list_videos(request):
    videos = Video.objects.all()
    return render(request, 'myapp/list_videos.html', {'videos': videos})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'myapp/list_authors.html', {'authors': authors})