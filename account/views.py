from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class RegistrationView(CreateView):
    template_name = "registration/registr.html"
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    

# Create your views here.
