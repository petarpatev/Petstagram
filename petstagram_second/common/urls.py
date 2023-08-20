from django.urls import path

from petstagram_second.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
