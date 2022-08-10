from django.shortcuts import render
# Create your views here.

def setCookies(request):
    response = render(request,'setcookies.html')
    # response.set_cookie('name','sonam')
    response.set_cookie('name','sonam',max_age=15)
    return response

def getCookies(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name','this is field for default cookies if name is empty')
    return render(request,'getcookies.html',{'name':name})



def delCookies(request):
    response = render(request,'deletecookies.html')
    response.delete_cookie('name')
    return response


# for signed cookies
def setSignedCookies(request):
    response = render(request,'setcookies.html')
    # response.set_cookie('name','sonam')
    response.set_signed_cookie('name','sonam',salt= 'salted')
    return response

def getSignedCookies(request):
    name = request.get_signed_cookie('name',salt='salted')
    return render(request,'getcookies.html',{'name':name})



def delSignedCookies(request):
    response = render(request,'deletecookies.html')
    response.delete_cookie('name')
    return response
