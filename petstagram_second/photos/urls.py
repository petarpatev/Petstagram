from django.urls import path

from petstagram_second.photos.views import photo_create, photo_details, photo_edit, photo_delete

urlpatterns = (
    path('add/', photo_create, name='photo create'),
    path('<int:pk>/', photo_details, name='photo details'),
    path('<int:pk>/edit/', photo_edit, name='photo edit'),
    path('<int:pk>/delete/', photo_delete, name='photo delete'),
)
