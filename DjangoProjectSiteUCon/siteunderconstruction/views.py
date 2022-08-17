from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request,'homepage.html')

def aboutView(request):
    return render(request,'about.html')