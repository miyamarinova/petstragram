from django.urls import path,include
from petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailView, PetPhotoEditView

urlpatterns = [
    path('create/', PetPhotoCreateView.as_view(), name='create photo'),
    path('edit/<int:pk>/', PetPhotoEditView.as_view(), name='edit photo'),
    path('<int:pk>/', include([
        path('', PetPhotoDetailView.as_view(), name='details photo'),
    ])),

]