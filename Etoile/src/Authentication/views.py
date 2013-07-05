# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render
from django.contrib.auth import logout


def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/authentication/loggedin/')
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)
    
def authenticate_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    nextpath = request.POST.get('nextpath','')
    user = authenticate(username=username, password=password)
    if(nextpath is None):
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                request.session['username'] = username
                request.session['password'] = password
                return HttpResponseRedirect('/authentication/loggedin/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
        return HttpResponseRedirect('/authentication/invalid/')
    else:
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                request.session['username'] = username
                request.session['password'] = password
                return HttpResponseRedirect(nextpath)
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
        return HttpResponseRedirect(nextpath)
         
def loggedin_view(request):
    return render(request, 'loggedin.html', {'full_name': request.user.username})


def logout_view(request):
    logout(request)
    nextpath = request.POST.get('nextpath','')
    if(nextpath is not None):
        return HttpResponseRedirect(nextpath)
    return render(request, 'logout.html')


def invalid_view(request):
    return render(request, 'invalid_login.html')
