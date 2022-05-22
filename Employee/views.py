from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from Employee.forms import EmployeeCreationForm
from Employee.models import Employee, FamilyDetail, PreviousOrganization


class EmployeeListView(View):
    def get(self, request, *args, **kwargs):


        employee_list = Employee.objects.all()    
        context = {'employee_list' : employee_list}
        return render(request,'index.html', context)


class EmployeeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = EmployeeCreationForm()

        context = {'form':form}
        return render(request, 'employee_create.html',context)
    def post(self, request, *args, **kwargs):
        
        totallength = request.POST['totallength']
        employee = Employee.objects.create(name=request.POST['employee_name'], salary=request.POST['employee_salary'], joining_date=request.POST['employee_joining_date'])
        employee.save()

        flag = 0
        member = memberrelation = profession = Organizationname = Description = ''
        
        for i in range(0, int(totallength)+1):
            if request.POST['member'+str(i)]:
                member = request.POST['member'+str(i)]
                flag = 1
            if request.POST['memberrelation'+str(i)]:
                memberrelation = request.POST['memberrelation'+str(i)]
                flag = 1
            
            if request.POST['profession'+str(i)]:
                profession = request.POST['profession'+str(i)]
                flag = 1
            if request.POST['Organizationname'+str(i)]:
                Organizationname = request.POST['Organizationname'+str(i)]
                flag = 1
            if request.POST['Description'+str(i)]:
                Description = request.POST['Description'+str(i)]
                flag = 1
            if flag == 1:
                family_detail = FamilyDetail.objects.create(employees = employee, name=member, relation_with_employee = memberrelation, profession=profession)
                family_detail.save()
                previous_organization = PreviousOrganization.objects.create(employees = employee, organization_name = Organizationname, description=Description)
                previous_organization.save()

        return redirect('employee_list')

class EmployeeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return redirect('employee_list')
    

class EmployeeUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('update view')