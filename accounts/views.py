from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, LoginForm

# Create your views here.

def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('get-product')
            else:
                return redirect('register')
    else:
        form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')