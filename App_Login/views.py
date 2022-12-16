from django.shortcuts import render
from django.urls import reverse
from .forms import SignupForm,UserUpdateForm,Profile_pics
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
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
            return HttpResponseRedirect(reverse('App_Login:login'))
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
                return HttpResponseRedirect(reverse('App_Login:user_profile'))
    else:
        form = AuthenticationForm()
    dict = {'form':form}
    return render(request,'App_Login/user_login.html',context=dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))

@login_required
def user_profile(request):
    dict = {}
    return render(request,'App_Login/profile.html',context=dict)
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Updated Successfully!')
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    else:
        form = UserUpdateForm(instance=request.user)
    dict = {'form':form}
    return render(request,'App_Login/update_profile.html',context=dict)

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Password Changed Successfully!')
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    else:
        form = PasswordChangeForm(user=request.user)
    dict = {'form':form}
    return render(request,'App_Login/password.html',context=dict)

@login_required
def add_profile_pic(request):
    if request.method == 'POST':
        form = Profile_pics(request.POST,request.FILES)
        if form.is_valid():
            user_object = form.save(commit=False)
            user_object.user = request.user
            user_object.save()
            messages.success(request,'profile picture successfully changed!')
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    else:
        form = Profile_pics()
    dict = {'form':form}
    return render(request,'App_Login/add_profile_pic.html',context=dict)
        
@login_required
def change_pro_pic(request):
    if request.method == 'POST':
        form = Profile_pics(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.success(request,'profile picture successfully changed!')
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    else:
        form = Profile_pics()
    dict = {'form':form}
    return render(request,'App_Login/add_profile_pic.html',context=dict)