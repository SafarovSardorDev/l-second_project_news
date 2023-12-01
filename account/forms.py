from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms


class RegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    
    class Meta :
        model = User
        fields =['username', 'password1' , 'password2', 'first_name', 'last_name', 'email']
       