from django.shortcuts import render, redirect

from petstagram_second.common.forms import CommentForm
from petstagram_second.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram_second.photos.models import Photo


def photo_create(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            form.save()
            # form._save_m2m()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    all_photo_likes = photo.like_set.all()
    is_photo_liked_by_user = all_photo_likes.filter(user=request.user)
    comment_form = CommentForm()
    all_photo_comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'comment_form': comment_form,
        'all_photo_likes': all_photo_likes,
        'all_photo_comments': all_photo_comments,
        'is_photo_liked_by_user': is_photo_liked_by_user,
    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk=photo.pk)

    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('index')
