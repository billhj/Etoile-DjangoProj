# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def login_view(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return render(request, 'login.html', {'state':state, 'username': username})
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'login.html', {'state':state, 'username': username})

def authenticate_view(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return render(request, 'login.html', {'state':state, 'username': username})
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'login.html', {'state':state, 'username': username})
            # Return an 'invalid login' error message.
            
        
from django.contrib.auth import logout

def logout_view(request):
    logout(request)