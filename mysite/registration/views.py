from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
 
def displaystudent (request):
    return render(request, "student.html")

def updatesstudent(request):
    return render (request,"update.html")

def deletestudent(request):
    return render (request,"delete.html")

def coursedisplay(request):
    return render (request,"coursedisplay.html") 

def deptdisplay(request):
    return render(request,"deptdisplay.html")

def facultydisplay(request):
    return render(request,"facultydispaly.html")