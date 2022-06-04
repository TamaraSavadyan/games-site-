from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Account
from django.views import View


class AccountView(View):
    def get(self, request):
        return render(request, 'accounts/account.html', {})

class AccountCreate(CreateView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success:success_page')


class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success:success_page')


class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success:success_page')
