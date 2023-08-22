from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from petstagram_second.accounts.forms import RegisterUserForm
from django.contrib.auth import views as auth_views


class RegisterUserView(generic.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form = super().form_valid(form)
        login(self.request, self.object)
        return form


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # next_page = reverse_lazy('index')


class LogoutUserView(auth_views.LogoutView):
    # next_page = reverse_lazy('user login')
    pass


def user_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def user_edit(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def user_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
