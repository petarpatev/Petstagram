from django.shortcuts import render

from petstagram_second.pets.models import Pet


def pet_create(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).get()
    all_pet_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_pet_photos': all_pet_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')

