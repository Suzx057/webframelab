from django.contrib import admin
from .models import Person, Student, Teacher

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'subject')