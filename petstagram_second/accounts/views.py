from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from petstagram_second.accounts.forms import RegisterUserForm, EditUserForm
from django.contrib.auth import views as auth_views

UserModel = get_user_model()


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
    user = UserModel.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditUserForm(instance=user)
    else:
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user details', pk=user.pk)

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'accounts/profile-edit-page.html', context)


def user_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
