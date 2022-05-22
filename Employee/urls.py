



from django.contrib import admin
from django.urls import path, include
from Employee import views
from .views import EmployeeListView, EmployeeCreateView, EmployeeDeleteView, EmployeeUpdateView

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employee_list"),
    path('create/', EmployeeCreateView.as_view(), name="employee_create"),
    path('update/', EmployeeUpdateView.as_view(), name="employee_update"),
    path('delete/', EmployeeDeleteView.as_view(), name="employee_delete"),
]