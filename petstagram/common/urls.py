from django.conf import settings

from django.urls import path, include
from petstagram.common.views import IndexView, like_pet_photo, share_pet_photo, add_comment

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pet_photo_like/<int:pk>/', like_pet_photo, name="like_pet_photo"),
    path('pet_photo_share/<int:pk>/', share_pet_photo, name="share_pet_photo"),
    path('pet_photo_comment/<int:pk>/', add_comment, name='add comment')
]