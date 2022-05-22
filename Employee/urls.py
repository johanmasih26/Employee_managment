



from django.contrib import admin
from django.urls import path, include
from Employee import views
from .views import EmployeeListView, EmployeeCreateView, EmployeeDeleteView, EmployeeUpdateView, EmployeeSearchView

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employee_list"),
    path('create/', EmployeeCreateView.as_view(), name="employee_create"),
    path('update/<str:pk>', EmployeeUpdateView.as_view(), name="employee_update"),
    path('delete/<str:pk>', EmployeeDeleteView.as_view(), name="employee_delete"),
    path('search/', EmployeeSearchView.as_view(), name="employee_search"),
]
