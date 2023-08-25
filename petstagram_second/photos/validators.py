from django.core.exceptions import ValidationError


def image_max_size_validator(image_obj):
    filesize = image_obj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')
