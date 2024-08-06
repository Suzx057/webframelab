# authors/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
from .forms import AuthorForm, AuthorFormSet

def author_formset_view(request):
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse('Formset submitted!')
    else:
        formset = AuthorFormSet(queryset=Author.objects.filter(first_name__startswith='A'))
    return render(request, 'authors/author_formset.html', {'formset': formset})

def author_list_view(request):
    authors = Author.objects.filter(first_name__startswith='A').order_by('first_name')
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_video_view(request):
    authors = Author.objects.filter(video_title__startswith='A')        
    return render(request, 'authors/author_video.html', {'authors': authors})

    
    