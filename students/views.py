
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Student, Course
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course


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

