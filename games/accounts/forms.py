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











#     <!-- {% block content }
# <form class="container" style="margin: 15px;" method="post">
#   {% csrf_token }
#   <div class="mb-3">
#     <label for="exampleInputEmail1" class="form-label">Email address</label>
#     <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value="{{ form.email }}">
#     <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
#   </div>
#   <div class="mb-3">
#     <label for="exampleInputPassword1" class="form-label">Username</label>
#     <input type="user" class="form-control" id="exampleInputPassword1" value="{{ form.username }}">
#   </div>
#   <div class="mb-3">
#     <label for="exampleInputPassword1" class="form-label">Password</label>
#     <input type="password" class="form-control" id="exampleInputPassword1" value="{{ form.password }}">
#   </div>
#   <div class="mb-3">
#     <label for="exampleInputPassword1" class="form-label">Repeat Password</label>
#     <input type="password" class="form-control" id="exampleInputPassword1">
#   </div>
#   <button type="submit" class="btn btn-success">Sign Up</button>
#   <a href="{% url 'home' %}"><button class="btn btn-danger" type="button">Cancel</button></a>
# </form>
# {% endblock } -->


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['info', 'profile_pic']
