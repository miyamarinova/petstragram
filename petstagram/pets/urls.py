from django.urls import path, include
from petstagram.pets.views import CreatePetView,DetailsPetView, DeletePetView, EditPetView

urlpatterns = [
    path('create/', CreatePetView.as_view(), name='create pet'),
    path('<str:username>/pet/<slug:pet_slug>/', DetailsPetView.as_view(), name='details pet'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', EditPetView.as_view(), name='edit pet'),
    path('<str:username>/pet/<slug:pet_slug>/',
         include([
             path('delete/', DeletePetView.as_view(), name='delete pet'),
         ])),

]