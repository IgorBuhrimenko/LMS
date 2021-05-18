import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Student, Lecturer, Group , Message


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="groups.csv"'
        writer = csv.writer(response)
        header = ['Course', 'Teacher', 'Students']
        writer.writerow(header)
        for group in queryset:
            lector_name = f'{group.teacher.first_name} {group.teacher.last_name}'
            students = []
            for student in group.students.all():
                student_name = f'{student.first_name} {student.last_name}'
                students.append(student_name)
            row = [group.course,
                   lector_name,
                   students
                   ]
            writer.writerow(row)
        return response

    export.short_description = 'Export group'


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        writer = csv.writer(response)
        header = ['full_name', 'email']
        writer.writerow(header)
        for student in queryset:
            full_name = f'{student.first_name} {student.last_name}'
            row = [full_name,
                   student.email
                   ]
            writer.writerow(row)
        return response

    export.short_description = 'Export students'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'course', 'teacher')
    filter_horizontal = ('students',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text_message']

