from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from datetime import timedelta

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.

from .models import Student, Lecturer, Group
from .forms import MessageForm
from .tasks import send_email

STUDENTS_PER_PAGE = 10
LECTURER_PER_PAGE = 4


def index(request):
    return render(request, 'academy/index.html')


def get_students(request):
    students = Student.objects.all().order_by()
    paginator = Paginator(students, STUDENTS_PER_PAGE)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, 'academy/get_students.html', {'title': 'Студенты', 'students': students, 'page': page})


def get_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'academy/get_student.html', {'student': student})


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'academy/create_student.html'
    fields = ['first_name', 'last_name', 'email']


class StudentEditView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'academy/edit_student.html'
    fields = ['first_name', 'last_name', 'email']


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'academy/delete_student.html'
    success_url = reverse_lazy('all_students')


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by()
    paginator = Paginator(lecturers, LECTURER_PER_PAGE)
    page = request.GET.get('page')
    try:
        lecturers = paginator.page(page)
    except PageNotAnInteger:
        lecturers = paginator.page(1)
    except EmptyPage:
        lecturers = paginator.page(paginator.num_pages)
    return render(request, 'academy/get_lecturers.html', {'title': 'Преподователи', 'lecturers': lecturers, 'page': page})



def get_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    return render(request, 'academy/get_lecturer.html', {'lecturer': lecturer})


class LecturerCreateView(LoginRequiredMixin, CreateView):
    model = Lecturer
    template_name = 'academy/create_lecturer.html'
    fields = ['first_name', 'last_name', 'email']


class LecturerEditView(LoginRequiredMixin, UpdateView):
    model = Lecturer
    template_name = 'academy/edit_lecturer.html'
    fields = ['first_name', 'last_name', 'email']


class LecturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Lecturer
    template_name = 'academy/delete_lecturer.html'
    success_url = reverse_lazy('all_lecturers')


def get_groups(request):
    groups = Group.objects.all().order_by()
    return render(request, 'academy/get_groups.html', {'title': 'Groups', 'groups': groups})


def get_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    return render(request, 'academy/get_group.html', {'group': group})


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'academy/create_group.html'
    fields = ['course', 'students', 'teacher']


class GroupEditView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'academy/edit_group.html'
    fields = ['course', 'students', 'teacher']


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'academy/delete_group.html'
    success_url = reverse_lazy('all_groups')


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            sent = request.session.get('sent')
            if sent:
                message = f"Sorry, please try again after{request.session.get_expiry_age()} seconds"
                form = MessageForm()
            else:
                request.session.set_expiry(timedelta(seconds=180))
                message = "Message sent"
                send_email.delay(form.cleaned_data)
                form = MessageForm()
                request.session['sent'] = True
                request.session.modified = True

            return render(request, 'academy/send_message.html', {'form': form,
                                                                 'message': message,
                                                                 }
                          )
        else:
            return render(request, 'academy/send_message.html', {'form': form})
    else:
        form = MessageForm()
    return render(request, 'academy/send_message.html', {'form': form})
