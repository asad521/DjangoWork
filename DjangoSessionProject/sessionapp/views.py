from django.shortcuts import render
# Create your views here.


def setSession(request):
    request.session['password'] = 'Sonamissession'
    return render(request, 'setsession.html')


def getSession(request):
    # sessionCookie =request.session['password']
    sessionCookie = request.session.get("name", "defaultvalue")
    return render(request, 'getsession.html', {'sessionCookie': sessionCookie})


def delSession(request):
    if "password" in request.session:
        del request.session['password']
    return render(request,'deletesession.html')

