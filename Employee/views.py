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
    def get(self, request, *args, pk, **kwargs):

        employee_obj = Employee.objects.get(id=pk)    
        employee_family_details = FamilyDetail.objects.select_related().filter(employees= employee_obj).all()
        employee_previous_organizations = PreviousOrganization.objects.select_related().filter(employees= employee_obj).all()
        print(employee_previous_organizations)
        context = {
            'employee' : employee_obj,
            'employee_family_details': employee_family_details,
            'employee_previous_organizations': employee_previous_organizations
        }
        return render(request, 'employee_update.html', context)
    

    def post(self, request, *args, pk, **kwargs):
        employee = Employee.objects.get(id=pk)    
        employee.name= request.POST['employee_name']
        employee.salary= request.POST['employee_salary']
        if request.POST['employee_joining_date']:
            employee.joining_date = request.POST['employee_joining_date']
        employee.save()
        total_organizations = request.POST['total_organization']
        total_familyDetails = request.POST['total_familyDetails']


        flag = 0
        member = memberrelation = profession = Organizationname = Description = ''
        
        for i in range(1, int(total_familyDetails)+1):
            if request.POST['member'+str(i)]:
                member = request.POST['member'+str(i)]
                flag = 1
            if request.POST['memberrelation'+str(i)]:
                memberrelation = request.POST['memberrelation'+str(i)]
                flag = 1
            if request.POST['id'+str(i)]:
                pk = request.POST['id'+str(i)]
                flag = 1
            
            if request.POST['profession'+str(i)]:
                profession = request.POST['profession'+str(i)]
                flag = 1
            
            if flag==1:
                family_detail_obj = FamilyDetail.objects.select_related().get(id=pk)
                family_detail_obj.name = member
                family_detail_obj.relation_with_employee = memberrelation
                family_detail_obj.profession = profession
                family_detail_obj.save()


            
        
        for i in range(1, int(total_organizations)+1):
            
            if request.POST['Organizationname'+str(i)]:
                Organizationname = request.POST['Organizationname'+str(i)]
                flag = 1
            if request.POST['Description'+str(i)]:
                Description = request.POST['Description'+str(i)]
                flag = 1
            if request.POST['id'+str(i)]:
                pk = request.POST['id'+str(i)]
                flag = 1

            if flag == 1:
                Previous_organization_obj = PreviousOrganization.objects.select_related().get(id=pk)
                Previous_organization_obj.organization_name = Organizationname
                Previous_organization_obj.description = Description
                Previous_organization_obj.save()

        return redirect('employee_list')
        
