from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    
    confirm_password = forms.CharField(label="Confirm Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}), required=True)

    class Meta:
        model = User
        fields = ('username','password') #"__all__"

        widgets = {
            'username' : forms.TextInput(attrs={"class":"form-control"}),
            'password' : forms.PasswordInput(attrs={"class":"form-control"}),
        }


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password') # "__all__"

        widgets = {
            'username' : forms.TextInput(attrs={"class":"form-control"}),
            'password' : forms.PasswordInput(attrs={"class":"form-control"}),
        }


