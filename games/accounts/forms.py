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

    class Meta:
        model = Account
        fields = ['profile_pic', 'user', 'info']
        # 'User.username', 'User.email',

    # def __init__(self, *args, **kwargs):

    #     super(AccountForm, self).__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs['placeholder'] = ''
        # self.fields['password'].widget.attrs['placeholder'] = ''

        # self.fields['username'].help_text = None





