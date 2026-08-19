
from django.contrib import admin
from .models import Student, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student_id',
        'name',
        'email',
        'phone',
        'course',
        'date_of_birth',
    )

