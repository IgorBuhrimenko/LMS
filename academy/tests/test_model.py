from django.core.exceptions import ValidationError
from django.test import TestCase


from academy.models import Student, Lecturer, Group


class StudentModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.first_name = 'Student first name'
        cls.last_name = 'Student last name '
        cls.email = 'email@mail.com'

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        # print('tearDown')
        pass

    def test_successful_student_creation(self):
        student = Student(first_name=self.first_name, last_name=self.last_name, email=self.email)
        student.full_clean()

    def test_fail_student_creation(self):
        first_name = 'a'*101
        student = Student(first_name=first_name, last_name=self.last_name, email=self.email)
        expected_message = "{'first_name': ['Ensure this value has at most 100 characters (it has 101).']}"
        with self.assertRaisesMessage(ValidationError, expected_message):
            student.full_clean()

    def test_student_email_is_not_none(self):
        student = Student(first_name=self.first_name, last_name=self.first_name, email=None)
        expected_message = "{'email': ['This field cannot be null.']}"
        with self.assertRaisesMessage(ValidationError, expected_message):
            student.full_clean()


class LecturerModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.first_name = 'Lecturer first name'
        cls.last_name = 'Lecturer last name '
        cls.email = 'email@mail.com'

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_successful_lecturer_creation(self):
        lecturer = Lecturer(first_name=self.first_name, last_name=self.last_name, email=self.email)
        lecturer.full_clean()

    def test_fail_lecturer_creation(self):
        last_name = 'a'*101
        lecturer = Lecturer(first_name=self.first_name, last_name=last_name, email=self.email)
        expected_message = "{'last_name': ['Ensure this value has at most 100 characters (it has 101).']}"
        with self.assertRaisesMessage(ValidationError, expected_message):
            lecturer.full_clean()

    def test_lecturer_email_is_not_none(self):
        lecturer = Lecturer(first_name=self.first_name, last_name=self.first_name, email=None)
        expected_message = "{'email': ['This field cannot be null.']}"
        with self.assertRaisesMessage(ValidationError, expected_message):
            lecturer.full_clean()


class GroupModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.course = 'Course full name'
        cls.first_name = 'Ivan'
        cls.last_name = 'Ivanov'
        cls.email = 'IvanIvano@ss.com'
        cls.lecturer_id = 12
        cls.teacher = Lecturer.objects.create(
            first_name=cls.first_name,
            last_name=cls.last_name,
            email=cls.email,
        )
        cls.students = Student.objects.create(
            first_name=cls.first_name,
            last_name=cls.last_name,
            email=cls.email
        )

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_successful_group_creation(self):
        group = Group.objects.create(course=self.course, teacher=self.teacher)
        group.students.add(self.students)

    def test_group_course_name_not_very_long(self):
        course_name = 'a '*1000
        group = Group.objects.create(course=course_name, teacher=self.teacher)
        expected_message = "{'course': ['Ensure this value has at most 100 characters (it has 2000).']}"
        with self.assertRaisesMessage(ValidationError, expected_message):
            group.full_clean()
