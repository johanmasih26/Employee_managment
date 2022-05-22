from django.forms import ModelForm
from Employee.models import Employee

class EmployeeCreationForm(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'