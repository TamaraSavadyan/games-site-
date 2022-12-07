from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    template = 'home.html'
    
    def get(self, request):
        return render(request, self.template, {})

class SuccessView(View):
    def get(self, request):
        return render(request, 'success.html', {})

class Error404View(View):
    def get(self, request):
        return render(request, '404_page.html', {})        
