from django.db import models

# Create your models here.
Departmentlist=[
    ("software engineering","SOFTWARE ENGINEERING"),
    ("networking","NETWORKING"),
    ("information management","INFORMATION MANAGEMENT"),
    ("data science","DATA SCIENCE"),
]

class Faculty(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
       return f"{self.name}"
    
     
     
 
class Department(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False, choices=Departmentlist)
    facultyName=models.ForeignKey(Faculty, null=False, blank=False, on_delete=models.CASCADE)
    