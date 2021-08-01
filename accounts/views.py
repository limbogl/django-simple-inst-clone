from django.shortcuts import redirect, render
from .forms import *
from .models import Profile
from django.http import HttpResponse
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
        	login(request, user)
	        return redirect('profile')
        else:
	        messages.info(request, 'Username OR password is incorrect')


    context = {}
    return render(request, 'accounts/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

#Check
@login_required(login_url='login')
def profilePage(request):

    posts = request.user.profile.post_set.all()

    context={'posts':posts}
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def settingsPage(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'accounts/settings_account.html', context)