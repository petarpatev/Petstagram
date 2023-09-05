from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram_second.common.forms import CommentForm
from petstagram_second.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram_second.pets.models import Pet

UserModel = get_user_model()


@login_required
def pet_create(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            form.save()
            # form._save_m2m()
            return redirect('user details', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


@login_required
def pet_details(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).get()
    pet_owner = UserModel.objects.filter(username=username).get()
    all_pet_photos = pet.photo_set.all()
    comment_form = CommentForm()
    context = {
        'pet': pet,
        'pet_owner': pet_owner,
        'all_pet_photos': all_pet_photos,
        'comment_form': comment_form,
    }
    return render(request, 'pets/pet-details-page.html', context)


@login_required
def pet_edit(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).get()
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username, pet_name)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


@login_required
def pet_delete(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).get()
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            pet.delete()
            return redirect('user details', pk=request.user.pk)
    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'pets/pet-delete-page.html', context)
