from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})

class SuccessView(View):
    def post(self, request):
        return render(request, 'success.html', {})
