from django.shortcuts import render, HttpResponseRedirect
from django.urls.base import reverse
from .forms import UserRegisterForm, UserLoginForm
from .models import User
from django.views.generic import CreateView
from .validations import LoginValidation, RegisterValidation
from django.contrib.auth import login


# Create your views here.

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        print(form.data)
        register_data = RegisterValidation(form.data)
        print(register_data.validate())
        return HttpResponseRedirect(reverse('register'))

class UserLoginView(CreateView):
    model = User
    form_class = UserLoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        print(form.data)
        login_data = LoginValidation(form.data)
        user = login_data.validate()
        if user != None:
            print(login(self.request, user))
            print('user logged in!')
        return HttpResponseRedirect(reverse('login'))