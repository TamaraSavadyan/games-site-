from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class WordleView(LoginRequiredMixin, View):
    login_url = reverse_lazy('accounts:account_login')
    template = 'wordle/wordle.html'

    def get(self, request):
        return render(request, self.template, {})
        # return render(request, 'wordle/test_wordle.html', {})