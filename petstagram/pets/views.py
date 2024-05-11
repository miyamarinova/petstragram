from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import exceptions
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram.accounts.views import OwnerRequiredMixin
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from django.contrib.auth import mixins as auth_mixins
class PetCreateView(LoginRequiredMixin,views.CreateView):
    # `model` and `fields` in `CreateView` are only needed to
    # create a form with `modelform_factory`
    # model = Pet
    # fields = ("name", "date_of_birth", "pet_photo")
    form_class = PetCreateForm
    template_name = "pets/pet-add-page.html"

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": self.object.user.email,
            "pet_slug": self.object.slug,
        })
    def get_form(self,form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user
        return form

class PetEditView(OwnerRequiredMixin, views.UpdateView):
    model = Pet  # queryset = Pet.objects.all()
    form_class = PetEditForm
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "mimi"
        return context

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": "Mimi",
            "pet_slug": self.object.slug,
        })

class PetDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):
    # TODO: fix bad queries
    # model = Pet  # or `queryset`
    queryset = Pet.objects.all() \
        .prefetch_related("petphoto_set") \
        .prefetch_related("petphoto_set__photolike_set") \
        .prefetch_related("petphoto_set__pets")

    template_name = "pets/pet-details-page.html"
    # slug_field = "pet_slug" # name of field in Model
    slug_url_kwarg = "pet_slug"  # name of param in URL

class PetDeleteView(OwnerRequiredMixin, views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = "pets/pet-delete-page.html"
    slug_url_kwarg = "pet_slug"
    success_url = reverse_lazy("index")
    extra_context = {
        "username": "Mimi",
    }
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs




"""
 def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    pet_form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == "POST":
        pet_form.save()
        return redirect("index")

    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": pet,
    }

    return render(request, "pets/pet-delete-page.html", context)
    """

"""def create_pet(request):
    pet_form = PetCreateForm(request.POST or None)

    if request.method == "POST":
        if pet_form.is_valid():
            created_pet = pet_form.save()
            return redirect("details pet", username="Doncho", pet_slug=created_pet.slug)

    context = {
        "pet_form": pet_form,
    }

    return render(request, "pets/pet-add-page.html", context)
"""