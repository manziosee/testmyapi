from django.contrib import admin

from student.models import Course, Student
from .models import *
from registration.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Faculty)