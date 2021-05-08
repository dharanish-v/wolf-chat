from django.shortcuts import render
from .forms import UserRegisterForm
from .models import User
from django.views.generic import CreateView

# Create your views here.

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'