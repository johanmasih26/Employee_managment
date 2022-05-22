from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    joining_date = models.DateField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return self.name


class FamilyDetail(models.Model):
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    relation_with_employee = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class PreviousOrganization(models.Model):
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=50, null=True, blank=True)
    

    def __str__(self):
        return self.organization_name

































# class Director(models.Model):  
#     name = models.CharField(max_length=20)  
  
#     def __str__(self):  
#         return self.name  
# class Movie(models.Model):  
#     movie_title = models.CharField(max_length=150)  
#     release_year = models.IntegerField()  
#     director = models.ForeignKey(Director, on_delete = models.CASCADE, max_length=100)  
      
#     def __str__(self):  
#         return self.movie_title  
        





