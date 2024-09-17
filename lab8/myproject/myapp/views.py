from django.shortcuts import render, redirect
from .forms import UserProfileForm

def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserProfileForm()
    return render(request, 'user_profile_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')