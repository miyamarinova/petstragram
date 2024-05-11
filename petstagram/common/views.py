from petstagram.common.models import PhotoLike
from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from django.views import generic as views


# Create your views here.

#def index(request):
#   pet_name_pattern = request.GET.get('pet_name_pattern', None)
#
#    pet_photos = PetPhoto.objects.all()
#
#    if pet_name_pattern:
#        pet_photos = pet_photos.filter(pets__name__icontains=pet_name_pattern)
#
#    context = {
#        'pet_photos': pet_photos,
#        'pet_name_pattern': pet_name_pattern,
#    }
#    return render(request, template_name="common/home-page.html", context=context)

class IndexView(views.ListView):
    queryset = (PetPhoto.objects.all()
        .order_by("-created_at") \
        .prefetch_related("pets") \
        .prefetch_related("photolike_set"))

    template_name = "common/home-page.html"

    paginate_by = 2

    @property
    def pet_name_pattern(self):
        return self.request.GET.get("pet_name_pattern", None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_name_pattern"] = self.pet_name_pattern or ""
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        if pet_name_pattern:
            filter_query['pets__name__icontains'] = pet_name_pattern
        return queryset.filter(**filter_query)

def like_pet_photo(request, pk):
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        # dislike
        pet_photo_like.delete()
        pass
    else:
        #like
        PhotoLike.objects.create(pet_photo_id=pk)
        # redirect to the last visited page
    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")

def share_pet_photo(request, pk):
    # create link to be copied

    copy(request.META['HTTP_HOST'] + resolve_url('details_photo', pet_photo_id=pk))
