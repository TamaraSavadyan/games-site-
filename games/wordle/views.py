from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.


class WordleView(LoginRequiredMixin, View):
    # Verify that the current user is authenticated.
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return self.handle_no_permission()

    def get(self, request):
        return render(request, 'wordle/wordle.html', {})
        # return render(request, 'wordle/test_wordle.html', {})