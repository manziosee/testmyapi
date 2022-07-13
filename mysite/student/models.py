from distutils.command.upload import upload
import email
from tkinter import CASCADE
from django.db import models
from registration.models import *
# Create your models here.
Courselist=[
    ("java","JAVA"),
    ("web design","WEB DESIGN"),
    ("big data","BIG DATA"),
    ("tcp/ip","TCP/IP"),
    ("data structure","DATA STRUCTURE"),
    ("linux","LINUX"),
    ("web tech","WEB TECH")
]
class Student(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    email=models.EmailField(max_length=100, null=False, blank=False)
    dob=models.DateTimeField(null=False,blank=False)
    address=models.CharField(max_length=100, null=False, blank=False)
    ##Image=models.ImageField(upload_to="images")
    departmentName=models.ForeignKey(Department, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
         return f"{self.name} to {self.departmentName}"
       
class Course(models.Model):
    courseName=models.CharField(max_length=100, null=False, blank=False, choices=Courselist)
    courseDept=models.ForeignKey(Department, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
         return f"{self.courseName} to {self.courseDept}"