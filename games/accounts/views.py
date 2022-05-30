from re import A
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Account


# Create your views here.
class AccountCreate(CreateView):
    model = Account
    fields = '__all__'
    # success_url = reverse_lazy('hhh')


class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    fields = '__all__'


class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account 
    fields = '__all__'    