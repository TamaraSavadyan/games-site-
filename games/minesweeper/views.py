import imp
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
# Create your views here.


class MinesweeperView(LoginRequiredMixin,View):
    login_url = reverse_lazy('accounts:account_login')
    # template = 'minesweeper/minesweeper.html'
    template = 'minesweeper/minesweeper-2.html'

    def get(self, request):
        return render(request, self.template, {})
        # return render(request, 'minesweeper/test_minesweeper.html', {})