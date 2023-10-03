from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
# Create your views here.


class SudokuView(LoginRequiredMixin, View):
    login_url = reverse_lazy('accounts:account_login')
    template = 'sudoku/sudoku.html'
    

    def get(self, request):
        return render(request, self.template, {})
        # return render(request, 'sudoku/test_sudoku.html', {})