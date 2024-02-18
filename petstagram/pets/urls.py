from django.urls import path, include
from petstagram.pets.views import PetCreateView, PetDeleteView, PetDetailView, PetEditView

urlpatterns = [
    path('create/', PetCreateView.as_view(), name='create pet'),
    path('<str:username>/pet/<slug:pet_slug>/', PetDetailView.as_view(), name='details pet'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', PetEditView.as_view(), name='edit pet'),
    path('<str:username>/pet/<slug:pet_slug>/',
         include([
             path('delete/', PetDetailView.as_view(), name='delete pet'),
         ])),

]