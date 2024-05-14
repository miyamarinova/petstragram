from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import PetPhoto

UserModel = get_user_model()
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
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ['-created_at']

    # user -> ForeignKey to users
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        )

class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE,
    )
    # user -> ForeignKey to users
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )