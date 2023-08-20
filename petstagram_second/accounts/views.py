from django.shortcuts import render


def user_login(request):
    return render(request, 'accounts/login-page.html')


def user_register(request):
    return render(request, 'accounts/register-page.html')


def user_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def user_edit(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def user_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
