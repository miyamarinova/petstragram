from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from petstagram.core.models import IHaveUser

UserModel = get_user_model()
# Create your models here.

class Pet(IHaveUser, models.Model):
    MAX_NAME_LENGTH = 30
    MAX_PET_PHOTO_LENGTH = 500

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False
    )

    pet_photo = models.URLField(
        null=False,
        blank=False,
        max_length=MAX_PET_PHOTO_LENGTH,
    )
    date_of_birth = models.DateField(
        null=False,
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')
        super().save(*args, **kwargs)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

