from django.contrib.auth import get_user_model
from django.db import models

from petstagram_second.photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    TEXT_MAX_LENGTH = 300

    comment_text = models.TextField(
        null=False,
        blank=False,
        max_length=TEXT_MAX_LENGTH,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
