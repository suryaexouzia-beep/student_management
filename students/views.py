from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import  redirect


def logout_user(request):
    logout(request)
    return redirect("home")
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            return render(
                request,
                "students/home.html",
                {
                    "students": Student.objects.all(),
                    "courses": Course.objects.all(),
                    "login_error": "Invalid username or password"
                }
            )

    return redirect("home")


def logout_user(request):
    logout(request)
    return redirect("login")
# API
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Home page
def home(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    course_id = request.GET.get("course")

    if course_id:
        students = students.filter(course_id=course_id)

    return render(
        request,
        "students/home.html",
        {
            "students": students,
            "courses": courses,
            "selected_course": course_id,
        }
    )


# Update student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()

    if request.method == "POST":
        student.student_id = request.POST["student_id"]
        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.phone = request.POST["phone"]
        student.course_id = request.POST["course"]
        student.date_of_birth = request.POST["date_of_birth"]
        student.address = request.POST["address"]
        student.save()

        return redirect("home")

    return render(
        request,
        "students/update_student.html",
        {
            "student": student,
            "courses": courses,
        }
    )


# Delete student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("home")

    return render(
        request,
        "students/delete_student.html",
        {"student": student}
    )