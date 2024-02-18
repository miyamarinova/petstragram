from django.urls import path,include
from petstagram.photos.views import PetPhotoCreateView, details_photo, edit_photo

urlpatterns = [
    path('create/', PetPhotoCreateView.as_view(),name='create photo'),
    path('<int:pk>/',
         include([
             path('', details_photo,name='details photo'),
             path('edit/',edit_photo,name='edit photo'),
    ]),
         )

]