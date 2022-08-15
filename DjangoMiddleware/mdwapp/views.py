from django.shortcuts import render,HttpResponse

# Create your views here.

def homepage(request):
    print("i am view")
    return HttpResponse("This is home page")
