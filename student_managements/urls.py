
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet, CourseViewSet
from students import views

router = DefaultRouter()

router.register(r"students", StudentViewSet)
router.register(r"courses", CourseViewSet)

urlpatterns = [
    path("", views.home, name="home"),

    path("admin/", admin.site.urls),

    path("api/", include(router.urls)),

    # Login / Logout
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # Student operations
    path(
        "student/update/<int:id>/",
        views.update_student,
        name="update_student"
    ),

    path(
        "student/delete/<int:id>/",
        views.delete_student,
        name="delete_student"
    ),
]
