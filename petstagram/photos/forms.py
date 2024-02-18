from django.forms import forms
from petstagram.photos.models import PetPhoto


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'location', 'pets')


class PetPhotoCreateForm(PetPhotoBaseForm):
    pass
