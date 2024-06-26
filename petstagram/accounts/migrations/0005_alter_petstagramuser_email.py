# Generated by Django 4.2.13 on 2024-05-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that username already exists.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
