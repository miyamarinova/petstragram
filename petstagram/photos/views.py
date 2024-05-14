from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from petstagram.pets.views import OwnerRequiredMixin
from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto

class PetPhotoCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/photo-add-page.html"
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")
    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })
    def get_form(self,form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user
        return form

class PetPhotoDetailView(OwnerRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = "photos/photo-details-page.html"
    context_object_name = "photo"
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related("photolike_set", "photocomment_set", "pets")

class PetPhotoEditView(OwnerRequiredMixin, views.UpdateView):
    queryset = PetPhoto
    template_name = "photos/photo-edit-page.html"
    form_class = PetPhotoEditForm
    success_url = reverse_lazy("details photo")

