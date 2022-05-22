
from Employee.models import Employee,FamilyDetail,PreviousOrganization
from django.contrib import admin



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']


class FamilyDetailAdmin(admin.ModelAdmin):
    list_display = ['name','relation_with_employee','profession']

class PreviousOrganizationAdmin(admin.ModelAdmin):
    list_display = ['organization_name','description']



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(FamilyDetail, FamilyDetailAdmin)
admin.site.register(PreviousOrganization, PreviousOrganizationAdmin)



