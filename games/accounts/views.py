from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from .models import Account
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User

# viewing account
class AccountView(View):
    model = Account
    template = 'accounts/account.html'
    success_url = reverse_lazy('success')

    def get(self, request, pk):
        account = get_object_or_404(self.model, pk=pk)
        return render(request, 'accounts/account.html', {})

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
        ctx= {'process':'registered'}
        return redirect(self.success_url, ctx)   


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
        
        ctx = {'process':'logged in'}
        return redirect(self.success_url, kwargs=ctx)

# logging out from account
class AccountLogout(View):
    template = 'accounts/login.html'
    success_url = reverse_lazy('success_page')

    def get(self, request):
        logout(request)
        ctx = {'process':'logged out'}
        return redirect(self.success_url, kwargs=ctx)


# updating account
class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success_page')

# deleting account
class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success_page')
