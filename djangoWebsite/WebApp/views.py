from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
    course = get_object_or_404(AllCourses, pk=course_id)
    
    return render(request, 'technicalCourses/details.html', {'course':course})

def YourChoice(request, course_id):
    course = get_object_or_404(AllCourses, pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except (KeyError, AllCourses.DoesNotExist):
        return render(request, 'technicalCourses/details.html', {
            'course' : course,
            'error_message' : "Select a valid option"
        })
    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request, 'technicalCourses/details.html', {'course':course})
