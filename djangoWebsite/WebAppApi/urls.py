from django.urls import path
from . import views


urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employees'),
    path('employee-form/', views.EmployeeForm, name='employee-form'),
    path('employee-create/', views.EmployeeCreate, name='employee-create'),
]