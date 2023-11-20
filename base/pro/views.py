from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from django.contrib.auth import authenticate



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
def register(request):
    return render(request, 'register.html')
def home(request):
        return render(request, 'home.html')
