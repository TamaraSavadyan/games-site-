from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class MinesweeperView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'minesweeper/minesweeper.html', {})
        # return render(request, 'minesweeper/test_minesweeper.html', {})