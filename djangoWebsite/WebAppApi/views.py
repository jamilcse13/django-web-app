from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employees
from . serializers import EmployeesSerializer

# Create your views here.
class EmployeeList(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

def EmployeeForm(request):
    return render(request, 'employee_form.html')

def EmployeeCreate(request):
    mydictionary = {
            "first_name" : request.POST['firstName'],
            "last_name" : request.POST['lastName'],
            "emp_id" : request.POST['empId'],
        }
    return JsonResponse(mydictionary)