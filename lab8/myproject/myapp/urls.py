from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/', views.user_profile_view, name='user_profile'),
    path('success/', views.success_view, name='success'),
]