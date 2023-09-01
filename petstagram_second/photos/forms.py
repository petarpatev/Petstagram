from django import forms

from petstagram_second.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo_picture', 'description', 'location', 'tagged_pets',)


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('description', 'location', 'tagged_pets',)
