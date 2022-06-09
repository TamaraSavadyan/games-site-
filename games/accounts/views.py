from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from .models import Account
from .forms import AccountCreateForm, AccountLoginForm


class AccountView(View):
    model = Account
    template = 'accounts/account.html'
    success_url = reverse_lazy('success')

    def get(self, request, pk):
        account = get_object_or_404(self.model, pk=pk)
        return render(request, 'accounts/account.html', {})


class AccountLogin(View):
    template = 'accounts/login.html'
    success_url = reverse_lazy('success_page')

    def get(self, request):
        return render(request, self.template, {})
    
    def post(self, request):
        return redirect(self.success_url)

# class AccountCreate(CreateView):
#     model = Account
#     template_name = 'accounts/register.html'
#     fields = ['email', 'name', 'password']
#     success_url = reverse_lazy('success_page')


class AccountCreate(View):
    model = Account
    template = 'accounts/register.html'
    success_url = reverse_lazy('success')

    def get(self, request):
        form = AccountCreateForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = AccountCreateForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success_page')


class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success_page')
