from django.urls import path

from petstagram_second.common.views import index, like_functionality, share_functionality

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_pk>/', like_functionality, name='like'),
    path('share/<int:photo_pk>/', share_functionality, name='share'),
)
