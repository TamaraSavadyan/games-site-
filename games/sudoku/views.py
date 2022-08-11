from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class SudokuView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'sudoku/sudoku.html', {})
        # return render(request, 'sudoku/test_sudoku.html', {})