from django.urls import path
from . import views

app_name = 'WebApp'

urlpatterns = [
    path('technicalCourses/<int:course_id>/', views.Details, name='details'),
    path('', views.Courses, name='home-page'),
    path('<int:course_id>/your-choice', views.YourChoice, name='your-choice'),
]