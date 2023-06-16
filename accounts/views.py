from django.shortcuts import render 
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
class ChangepasswordPageView(generic.CreateView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password_change")
    template_name = "registration/password_change.html"
    
