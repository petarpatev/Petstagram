from django.urls import path

from petstagram_second.common.views import index, like_functionality, share_functionality, add_comment

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_pk>/', like_functionality, name='like'),
    path('share/<int:photo_pk>/', share_functionality, name='share'),
    path('comment/<int:photo_pk>/', add_comment, name='add comment'),
)
