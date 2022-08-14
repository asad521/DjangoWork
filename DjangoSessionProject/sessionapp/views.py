from django.shortcuts import render
# Create your views here.


def setSession(request):
    request.session['password'] = 'Sonam_is_session_value'
    request.session.set_expiry(15) 
    request.session.set_expiry(0)
    return render(request, 'setsession.html')


def getSession(request):
    # sessionCookie =request.session['password']
    sessionCookie = request.session.get("password", "defaultvalue")
    keys = request.session.keys()
    items = request.session.items()
    return render(request, 'getsession.html', {'sessionCookie': sessionCookie,'keys':keys,'items':items})


def delSession(request):
    
    request.session.flush()
    request.session.clear_expired()
    if "password" in request.session:
        del request.session['password']
    return render(request,'deletesession.html')

