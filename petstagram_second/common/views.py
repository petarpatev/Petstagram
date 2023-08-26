from django.shortcuts import render, redirect

from petstagram_second.common.models import Like
from petstagram_second.photos.models import Photo


def index(request):
    all_photo_posts = Photo.objects.all()
    context = {
        'all_photo_posts': all_photo_posts,
    }
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_pk):
    photo = Photo.objects.filter(pk=photo_pk).get()
    like_obj = Like.objects.filter(to_photo_id=photo_pk, user_id=request.user.pk).first()

    if like_obj:
        like_obj.delete()
    else:
        like = Like.objects.create(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')
