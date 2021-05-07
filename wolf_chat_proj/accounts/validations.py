from django.forms import Form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, widgets
from .models import Movie, User
from django.contrib.auth.hashers import make_password
import json

class RegisterValidation():

    def __init__(self, *args):
        self.args = args
        self.fields = self.args[0]
        if len(args) > 1:
            self.user = args[1]
            if self.user.id == None:
                self.user = 'NIL'

    def validate(self):
        try:
            self.username = self.fields['username']
            self.password = self.fields['password']
            self.confirm_password = self.fields['confirm_password']

        except Exception as e:
            print("malformed request!")

        if User.objects.filter(username=self.username).exists():
            print("username already exists")
            return 
        
        if self.password == self.confirm_password:
            user = User(username=self.username , password=make_password(self.password))
            user.save()

class LoginValidation():

    def __init__(self, *args):
        self.args = args
        self.fields = args[0]
        if len(args) > 1:
            self.user = args[1]
            if self.user.id == None:
                self.user = 'NIL'

    def validate(self):

        try:
            self.username = self.fields['username']
            self.password = self.fields['password']

        except Exception as e:
            print("malformed request!")

        user = User.objects.filter(username=self.username,password=make_password(self.password))[0]
        if user:
            return user