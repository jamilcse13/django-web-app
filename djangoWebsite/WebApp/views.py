from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import AllCourses
from django.template import loader

# Create your views here.
def Courses(request):
    all_courses = AllCourses.objects.all()
    template = loader.get_template('technicalCourses/courses.html')
    context = {
        'all_courses' : all_courses
    }
    return HttpResponse(template.render(context, request))

def Details(request, course_id):
    try:
        course = AllCourses.objects.get(pk=course_id)
    except AllCourses.DoesNotExist:
        raise Http404("Course Not Available")
    return render(request, 'technicalCourses/details.html', {'course':course})