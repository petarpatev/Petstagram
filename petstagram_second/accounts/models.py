from enum import Enum
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from petstagram_second.accounts.validators import only_alphabetical_letters_validator


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]

    @classmethod
    def max_len_genders(cls):
        return max([len(name) for name, _ in cls.choices()])


class GendersTypes(ChoicesMixin, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'


class PetstagramUser(auth_models.AbstractUser):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            only_alphabetical_letters_validator,
        ),
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            only_alphabetical_letters_validator,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        choices=GendersTypes.choices(),
        max_length=GendersTypes.max_len_genders(),
    )
