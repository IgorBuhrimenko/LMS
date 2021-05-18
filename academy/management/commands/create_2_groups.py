from django.core.management.base import BaseCommand

from faker import Faker

from academy.models import Student, Lecturer, Group


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker(['en_US'])
        number_of_students = 10
        number_of_groups = 2

        for i in range(number_of_groups):

            lecturer = Lecturer.objects.create(first_name=fake.unique.first_name(),
                                               last_name=fake.unique.last_name(),
                                               email=fake.email())
            lecturer.save()
            group = Group.objects.create(course=fake.job(), teacher=lecturer)

            for j in range(number_of_students):
                student = Student.objects.create(first_name=fake.unique.first_name(),
                                                 last_name=fake.unique.last_name(),
                                                 email=fake.email())
                student.save()
                group.students.add(student)
            group.save()
