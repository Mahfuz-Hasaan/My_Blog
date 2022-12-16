from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import UserProfile
class SignupForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = User
        fields = ['username','email',]

class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(label="Email Address", required=True)
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class Profile_pics(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']
    