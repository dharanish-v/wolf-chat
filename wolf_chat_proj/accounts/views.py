from django.shortcuts import render
from .forms import UserRegisterForm, UserLoginForm
from .models import User
from django.views.generic import CreateView

# Create your views here.

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'

class UserLoginView(CreateView):
    model = User
    form_class = UserLoginForm
    template_name = 'login.html'