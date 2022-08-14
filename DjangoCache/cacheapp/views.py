from django.shortcuts import render

# Create your views here.

def courseView(reqeust):
    return render (reqeust,'course.html')