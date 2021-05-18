from django.db import models
from django.urls import reverse

#Create Models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField('Имя студента', max_length=100)
    last_name = models.CharField('Фамилия студента', max_length=100)
    email = models.EmailField(max_length=250)
    cover = models.ImageField(upload_to='covers/student_photo', default='covers/student_photo/default.png')

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('student', kwargs={'student_id': self.student_id})


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField('Имя лектора', max_length=100)
    last_name = models.CharField('Фамилия лектора', max_length=100)
    email = models.EmailField(max_length=100)
    cover = models.ImageField(upload_to='covers/lector_photo', default='covers/lector_photo/turtle.png')

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('lecturer', kwargs={'lecturer_id': self.lecturer_id})


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField('Название предмета', max_length=100)
    students = models.ManyToManyField(Student)
    teacher = models.OneToOneField(Lecturer, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('group', kwargs={'group_id': self.group_id})


class Message(models.Model):
    name = models.CharField('Имя отправителя', max_length=100)
    email = models.EmailField(max_length=100)
    text_message = models.CharField('Текст меседжа', max_length=200)


    def __str__(self):
        return self.text_message

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'text_message': self.text_message
        }

