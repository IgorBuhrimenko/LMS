from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Student, Lecturer, Group


def index(request):
    return render(request, 'academy/index.html')

#Student View


def get_students(request):
    students = Student.objects.all().order_by()
    return render(request, 'academy/get_students.html', {'title': 'Студенты', 'students': students})


def get_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'academy/get_student.html', {'student': student})

#LecturerView


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by()
    return render(request, 'a ademy/get_lecturers.html', {'title': 'Студенты', 'lecturers': lecturers})


def get_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    return render(request, 'academy/get_lecturer.html', {'lecturer': lecturer})

#GroupView


def get_groups(request):
    groups = Group.objects.all().order_by()
    return render(request, 'academy/get_groups.html', {'title': 'Groups', 'groups': groups})


def get_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    return render(request, 'academy/get_group.html', {'group': group})
