from django.conf import settings

from django.urls import path, include
from petstagram.common.views import index, like_pet_photo, share_pet_photo

urlpatterns = [
    path('',index, name='index'),
    path('pet_photo_like/<int:pk>/', like_pet_photo, name="like_pet_photo"),
    path('pet_photo_share/<int:pk>/', share_pet_photo, name="share_pet_photo")
]