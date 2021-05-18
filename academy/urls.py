from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all_students', views.get_students, name='all_students'),
    path('all_students/<int:student_id>', views.get_student, name='student'),
    path('all_students/<int:pk>/edit', views.StudentEditView.as_view(), name='edit_student'),
    path('all_students/<int:pk>/del', views.StudentDeleteView.as_view(), name='delete_student'),
    path('all_students/new', views.StudentCreateView.as_view(), name='create_student'),
    path('all_lecturers', views.get_lecturers, name='all_lecturers'),
    path('all_lecturers/<int:lecturer_id>', views.get_lecturer, name='lecturer'),
    path('all_lecturer/new', views.LecturerCreateView.as_view(), name='create_lecturer'),
    path('all_lecturer/<int:pk>/edit', views.LecturerEditView.as_view(), name='edit_lecturer'),
    path('all_lecturer/<int:pk>/del', views.LecturerDeleteView.as_view(), name='delete_lecturer'),
    path('all_groups', views.get_groups, name='all_groups'),
    path('all_group/<int:group_id>', views.get_group, name='group'),
    path('all_group/new', views.GroupCreateView.as_view(), name='create_group'),
    path('all_group/<int:pk>/edit', views.GroupEditView.as_view(), name='edit_group'),
    path('all_group/<int:pk>/delete', views.GroupDeleteView.as_view(), name='delete_group'),
    path('send_message', views.send_message, name='send_message'),

]
