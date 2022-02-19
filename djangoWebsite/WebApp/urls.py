from django.urls import path
from . import views

urlpatterns = [
    path('technicalCourses/<int:course_id>/', views.Details, name='details'),
    path('', views.Courses, name='home-page'),
]