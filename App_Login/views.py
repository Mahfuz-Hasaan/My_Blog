from django.shortcuts import render
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.contrib.auth.decorators import login_required
def SignUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,'SignUp successfully done')
            messages.success(request, 'Account Created Successfully!')
            return HttpResponseRedirect(reverse('App_Blog:blog_list'))
    else:
        form = SignupForm()
    dict = {'form':form}
    return render(request,'App_Login/signup.html',context=dict)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in succcessfully!')
                return HttpResponseRedirect(reverse('App_Blog:blog_list'))
    else:
        form = AuthenticationForm()
    dict = {'form':form}
    return render(request,'App_Login/user_login.html',context=dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))