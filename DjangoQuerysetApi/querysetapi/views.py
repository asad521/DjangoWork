from django.shortcuts import render
from .models import Students
# Create your views here.
def homepage(request):
    students_data  = Students.objects.all()
    
    return render(request,'home.html' , {'students':students_data})
