from django.db import models

# Create your models here.
class AllCourses(models.Model):
    course_name = models.CharField(max_length=200)
    instructor_name = models.CharField(max_length=100)
    def __str__(self):
        return self.course_name

class Details(models.Model):
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)
    def __str__(self):
        return str(self.pk)