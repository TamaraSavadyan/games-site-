from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class WordleView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'wordle/wordle.html', {})
        # return render(request, 'wordle/test_wordle.html', {})