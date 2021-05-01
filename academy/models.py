from django.db import models

#Create Models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField('Имя студента', max_length=100)
    last_name = models.CharField('Фамилия студента', max_length=100)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.last_name


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField('Имя лектора', max_length=100)
    last_name = models.CharField('Фамилия лектора', max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.last_name


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField('Название предмета', max_length=100)
    students = models.ManyToManyField(Student)
    teacher = models.OneToOneField(Lecturer, on_delete=models.CASCADE)
# Create your models here.
