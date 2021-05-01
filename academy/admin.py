from django.contrib import admin
from .models import Student, Lecturer, Group


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'course', 'teacher')
    filter_horizontal = ('students',)
