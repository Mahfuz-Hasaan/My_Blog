from django.shortcuts import render
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import  HttpResponseRedirect
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