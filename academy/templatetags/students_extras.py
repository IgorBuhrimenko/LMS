from django import template
from ..models import Group

register = template.Library()


@register.filter()
def get_count_students(value):
    group = Group.objects.filter(course=value)[0]
    return f'{value} ({group.students.count()})'
