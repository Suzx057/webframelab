from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required



from django.contrib.sessions.models import Session

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # ตรวจสอบผู้ใช้และรหัสผ่าน
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # ล็อกอินผู้ใช้และสร้างเซสชัน
                login(request, user)

                # เพิ่ม session_key ลงในเซสชัน
                request.session['session_key'] = request.session.session_key
                
                return redirect('show_videos')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    # ลบข้อมูล session
    try:
        del request.session['member_id']
        del request.session['member_username']
    except KeyError:
        pass
    return redirect('login')

@login_required
def show_videos(request):
    # ดึงข้อมูลชื่อผู้ใช้จากผู้ใช้ที่ล็อกอินอยู่
    username = request.user.username
    # ดึงค่า session_key
    session_key = request.session.get('session_key', 'No session key available')
    
    return render(request, 'videos.html', {'username': username, 'session_key': session_key})