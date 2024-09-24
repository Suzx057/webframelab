from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # ใช้ฟังก์ชัน authenticate เพื่อตรวจสอบผู้ใช้และรหัสผ่าน
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # ล็อกอินผู้ใช้และสร้างเซสชัน
                login(request, user)
                return redirect('show_videos')  # เปลี่ยนเส้นทางตามที่คุณต้องการ
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
    return render(request, 'videos.html', {'username': username})