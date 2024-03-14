from django.shortcuts import render
from django.urls import reverse
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
    queryset = PetPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("pets")

    template_name = "photos/photo-details-page.html"


class PetPhotoEditView(OwnerRequiredMixin, views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    template_name = "photos/photo-edit-page.html"
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })