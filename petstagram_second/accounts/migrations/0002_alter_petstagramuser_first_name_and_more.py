# Generated by Django 4.2.4 on 2023-09-03 09:09

import django.core.validators
from django.db import migrations, models
import petstagram_second.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), petstagram_second.accounts.validators.only_alphabetical_letters_validator]),
        ),
        migrations.AlterField(
            model_name='petstagramuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), petstagram_second.accounts.validators.only_alphabetical_letters_validator]),
        ),
    ]
