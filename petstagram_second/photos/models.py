from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_second.pets.models import Pet
from petstagram_second.photos.validators import image_max_size_validator

UserModel = get_user_model()


class Photo(models.Model):
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 30

    photo_picture = models.ImageField(
        null=False,
        blank=False,
        validators=(
            image_max_size_validator,
        )
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=(
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        null=True,
        blank=True,
        max_length=LOCATION_MAX_LENGTH,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        null=False,
        blank=True,
        auto_now=True,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
