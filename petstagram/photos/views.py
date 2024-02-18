from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views

from petstagram.photos.forms import PetPhotoCreateForm
from petstagram.photos.models import PetPhoto

class PetPhotoCreateView(views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/photo-add-page.html"
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })


# Create your views here.
#def create_photo(request):
#    context={}
#    return render(request, template_name='photos/photo-add-page.html',context=context)

def details_photo(request, pk):
    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk)
    }
    return render(request, 'photos/photo-details-page.html',context)

def edit_photo(request, pk):
    context={}
    return render(request,template_name='photos/photo-edit-page.html',context=context)