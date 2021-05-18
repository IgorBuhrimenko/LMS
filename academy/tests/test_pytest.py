from django.urls import reverse
import pytest

from academy.models import Student, Lecturer, Group


# PyTest Student
@pytest.fixture
def create_students():
    def make_students(**kwargs):
        number_of_students = kwargs['number_of_students']
        students = []
        for student_num in range(number_of_students):
            student = Student.objects.create(
                first_name=f'Mike #{str(student_num)}',
                last_name=f'Tyson #{str(student_num)}',
                email=f'{str(student_num)}tyson@ss.com'
            )
            students.append(student)
        return students

    return make_students


@pytest.mark.django_db
def test_students_show(client, create_students):
    students = create_students(number_of_students=1)
    student = students[0]
    assert student.first_name, student.last_name is not None

    resp = client.get(reverse('student', kwargs={'student_id': student.student_id}))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_students_url_exists_at_desired_location(client):
    resp = client.get('/all_students')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_students_url_accessible_by_name(client):
    resp = client.get(reverse('all_students'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_lists_all_students(client, create_students):
    number_of_students = 3
    create_students(number_of_students=number_of_students)
    resp = client.get(reverse('all_students'))
    assert resp.status_code == 200
    assert len(resp.context['students']) == number_of_students


# PyTest Lecturer


@pytest.mark.django_db
def test_view_lecturers_url_exists_at_desired_location(client):
    resp = client.get('/all_lecturers')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_lecturers_url_accessible_by_name(client):
    resp = client.get(reverse('all_lecturers'))
    assert resp.status_code == 200


@pytest.fixture
def create_lecturers():
    def make_lecturer(**kwargs):
        numbers_of_lecturer = kwargs['number_of_lecturers']
        lecturers = []
        for lecturer_num in range(numbers_of_lecturer):
            lecturer = Lecturer.objects.create(
                first_name=f'Ivan{str(lecturer_num)}',
                last_name=f'Ivanov{str(lecturer_num)}',
                email=f'{str(lecturer_num)}ivi@ss.com'
            )
            lecturers.append(lecturer)
        return lecturers

    return make_lecturer


@pytest.mark.django_db
def test_lists_all_lecturers(client, create_lecturers):
    number_of_lecturers = 4
    create_lecturers(number_of_lecturers=number_of_lecturers)
    resp = client.get(reverse('all_lecturers'))
    assert resp.status_code == 200
    assert len(resp.context['lecturers']) == number_of_lecturers


@pytest.mark.django_db
def test_lecturers_show(client, create_lecturers):
    lecturers = create_lecturers(number_of_lecturers=1)
    lecturer = lecturers[0]
    assert lecturer.first_name, lecturer.last_name is not None

    resp = client.get(reverse('lecturer', kwargs={'lecturer_id': lecturer.lecturer_id}))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_groups_url_exists_at_desired_location(client):
    resp = client.get('/all_groups')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_groups_url_accessible_by_name(client):
    resp = client.get(reverse('all_groups'))
    assert resp.status_code == 200


@pytest.fixture
def create_groups():
    def make_groups(**kwargs):
        numbers_of_group = kwargs['numbers_of_group']
        numbers_of_students = kwargs['numbers_of_students']
        course = 'Astonomy'
        groups = []
        for number_group in range(numbers_of_group):
            teacher = Lecturer.objects.create(
                first_name=f'first name {number_group}',
                last_name=f'last name {number_group}',
                email=f'email{number_group}',
            )
            group = Group.objects.create(course=course, teacher=teacher)
            for num_stud in range(numbers_of_students):
                student = Student.objects.create(first_name='Max', last_name='Kevin', email='studentmail@cc.com')
                group.students.add(student)
            groups.append(group)
        return groups
    return make_groups


@pytest.mark.django_db
def test_lists_all_group(client, create_groups):
    numbers_of_group = 10
    numbers_of_students = 10

    create_groups(numbers_of_group=numbers_of_group, numbers_of_students=numbers_of_students)
    resp = client.get(reverse('all_groups'))
    assert resp.status_code == 200
    assert len(resp.context['groups']) == numbers_of_group


@pytest.mark.django_db
def test_group_show(client, create_groups):
    numbers_of_group = 10
    numbers_of_students = 10
    groups = create_groups(numbers_of_group=numbers_of_group, numbers_of_students=numbers_of_students)
    group = groups[0]
    assert group.teacher, group.course is not None
    resp = client.get(reverse('group', kwargs={'group_id': group.group_id}))
    assert resp.status_code == 200
