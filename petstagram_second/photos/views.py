from django.shortcuts import render

from petstagram_second.photos.models import Photo


def photo_create(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    all_photo_likes = photo.like_set.all()
    all_photo_comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'all_photo_likes': all_photo_likes,
        'all_photo_comments': all_photo_comments,
    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
