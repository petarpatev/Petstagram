from django.core.exceptions import ValidationError


def only_alphabetical_letters_validator(value):
    if not value.isalpha():
        return ValidationError('Please, enter only letters.')
