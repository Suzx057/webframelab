from django.urls import path
from .views import PersonListView, StudentListView, TeacherListView

urlpatterns = [
    path('persons/', PersonListView.as_view(), name='person-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
]