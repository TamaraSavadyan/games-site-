from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from .models import Account
from .forms import RegisterForm
from django.contrib.auth.models import User


class AccountView(View):
    model = Account
    template = 'accounts/account.html'
    success_url = reverse_lazy('success')

    def get(self, request, pk):
        account = get_object_or_404(self.model, pk=pk)
        return render(request, 'accounts/account.html', {})


class AccountLogin(View):
    template = 'accounts/login.html'
    success_url = reverse_lazy('success_page')

    def get(self, request):
        return render(request, self.template, {})
    
    def post(self, request):
        return redirect(self.success_url)

# class AccountCreate(CreateView):
#     model = Account
#     template_name = 'accounts/register.html'
#     fields = ['email', 'name', 'password']
#     success_url = reverse_lazy('success_page')

# TODO: I'm here working on it 
class AccountCreate(View):
    model = User
    template = 'accounts/register.html'
    success_url = reverse_lazy('success_page')

    def get(self, request):
        form = RegisterForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)   

'''
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
'''

    # model = Account
    # template = 'accounts/register.html'
    # success_url = reverse_lazy('success')

    # def get(self, request):
    #     form = AccountCreateForm()
    #     ctx = {'form': form}
    #     return render(request, self.template, ctx)

    # def post(self, request):
    #     form = AccountCreateForm(request.POST)
    #     if not form.is_valid():
    #         ctx = {'form': form}
    #         return render(request, self.template, ctx)

    #     form.save()
    #     return redirect(self.success_url)


class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success_page')


class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'accounts/auth.html'
    fields = '__all__'
    success_url = reverse_lazy('success_page')
