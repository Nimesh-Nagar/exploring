from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta class gives neated name for configurations and keep the configurations in one place.
    # 
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


# model form : allows us to create a form that will work with a specifis database model .
# we need a form that update the user model. 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
