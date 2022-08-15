from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

# This is for My_Exception_middlware
def exceptionView(request):
    print('i am exception view')
    a = 10/0
    return HttpResponse("This is homepage   ")

# For process template repsonse middlware
def templateResponseView(request):
    context = {'name':"rahul"}
    return TemplateResponse(request,'templateresponse.html', context)
