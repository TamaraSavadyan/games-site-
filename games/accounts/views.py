from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from .models import Account
from .forms import (
        AccountForm, 
        RegisterForm, 
        LoginForm, 
        UpdateUserForm, 
        UpdateAccountForm
    )
from django.contrib.auth.models import User


# viewing account
class AccountView(LoginRequiredMixin, View):
    model = Account
    template = 'accounts/account.html'

    def get(self, request, username):
        form = AccountForm(instance=request.user)
        ctx = {'form': form}
        return render(request, self.template, ctx)


# creating new account (registration)
class AccountCreate(View):
    model = User
    template = 'accounts/register.html'
    success_url = reverse_lazy('success_page')

    def get(self, request):
        form = RegisterForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        # ctx= {'process':'registered'}
        request.session['process'] = 'registered to'
        return redirect(self.success_url)


# logging into existing account
class AccountLogin(View):
    template = 'accounts/login.html'
    success_url = reverse_lazy('success_page')

    def get(self, request):
        form = LoginForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

        else:
            messages.success(request, ("There was an error logging in, try again"))
            ctx = {'form': form}
            return render(request, self.template, ctx)

        # ctx = {'process':'logged in'}
        request.session['process'] = 'logged in'
        return redirect(self.success_url)


# logging out from account
class AccountLogout(View):
    success_url = reverse_lazy('success_page')

    def get(self, request):
        logout(request)

        # ctx = {'process':'logged out'}
        request.session['process'] = 'logged out from'
        return redirect(self.success_url)


# updating account
class AccountUpdate(LoginRequiredMixin, View):
    template = 'accounts/update.html'
    account_template = 'accounts/account.html'
    success_url = reverse_lazy('success_page')

    def get(self, request, username):
        user_form = UpdateUserForm()
        account_form = UpdateAccountForm()    
        
        ctx = {
                'user_form': user_form,
                'account_form': account_form
            }
        return render(request, self.template, ctx)

    def post(self, request, username):
        # print(request.user, request.user.account)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        account_form = UpdateAccountForm(request.POST, request.FILES, instance=request.user.account)    

        if not user_form.is_valid() and not account_form.is_valid():
            user_form = UpdateUserForm(instance=request.user)
            account_form = UpdateAccountForm(instance=request.user.account)

            return render(request, self.template, {'user_form': user_form, 'account_form': account_form})
        
        user_form.save()
        account_form.save()

        request.session['process'] = 'updated at'
        return redirect(self.success_url)


# deleting account
class AccountDelete(LoginRequiredMixin, View):
    template = 'accounts/delete.html'
    success_url = reverse_lazy('success_page')

    def get(self, request, username):
        ctx = {}
        return render(request, self.template, ctx)

    def post(self, request, username):
        u = User.objects.get(username=username)
        u.delete()
        
        request.session['process'] = 'deleted from'
        return redirect(self.success_url)    


