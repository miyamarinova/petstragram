from django.db import models

from petstagram.photos.models import PetPhoto


# Create your models here.
class PhotoComment(models.Model):
    MAX_LENGTH = 300

    text = models.TextField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING,
    )

    # user -> ForeignKey to users

class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING,
    )

    # user -> ForeignKey to users