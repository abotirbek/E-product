from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, LoginForm, ProfileForm
from .models import Profile

# Create your views here.

def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user = user)
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
                return redirect('get-product')
            else:
                return redirect('register')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def get_profile(request):
    user = request.user
    if user:
        profile = Profile.objects.get(user=user)
    else:
        return redirect('get-product')
    return render(request, 'accounts/profile.html', {'profile': profile})

def edit_profile(request):
    profile = None
    user = request.user
    if user:
        profile = Profile.objects.get(user = user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance = profile)
    return render(request, 'accounts/edit_profile.html', {'form':form})