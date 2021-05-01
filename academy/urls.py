from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all_students', views.get_students, name='all_students'),
    path('all_students/<int:student_id>', views.get_student, name='student'),
    path('all_lecturers', views.get_lecturers, name='all_lecturers'),
    path('all_lecturers/<int:lecturer_id>', views.get_lecturer, name='lecturer'),
    path('all_groups', views.get_groups, name='all_groups'),
    path('all_group/<int:group_id>', views.get_group, name='group'),
]
