from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .models import Account
from .forms import AccountForm


class AccountView(View):
    model = Account
    template = 'accounts/account.html'
    success_url = reverse_lazy('success')

    def get(self, request, pk):
        account = get_object_or_404(self.model, pk=pk)
        return render(request, 'accounts/account.html', {})


class AccountLogin(View):
    def get(self, request):
        return render(request, 'accounts/login.html', {})

# class AccountCreate(CreateView):
#     model = Account
#     template_name = 'accounts/register.html'
#     fields = '__all__'
#     success_url = reverse_lazy('success_page')


class AccountCreate(View):
    model = Account
    template = 'accounts/register.html'
    success_url = reverse_lazy('success')

    def get(self, request):
        form = AccountForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = AccountForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
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
    success_url = reverse_lazy('success:success_page')
