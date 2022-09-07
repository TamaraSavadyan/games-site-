from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    #     labels = {
    #         'username': 'Username',
    #         'email': 'Email',
    #         'password1': 'Password',
    #         'password2': 'Password confirmation',
    #     }
    
    def __init__(self, *args, **kwargs):

        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['password1'].widget.attrs['placeholder'] = '' 
        self.fields['password2'].widget.attrs['placeholder'] = ''


class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):

        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['password'].widget.attrs['placeholder'] = ''

        self.fields['username'].help_text = None


class AccountForm(ModelForm):
    profile_pic = forms.ImageField() # widget=forms.FileInput(attrs={'class': 'form-control-file'})
    info = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8}))

    class Meta:
        model = Account
        fields = ['profile_pic', 'info']
    

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateAccountForm(forms.ModelForm):
    profile_pic = forms.ImageField()
    info = forms.CharField()

    class Meta:
        model = Account
        fields = ['profile_pic', 'info']