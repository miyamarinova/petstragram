from petstagram.common.models import PhotoLike
from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy


# Create your views here.
def index(request):
    pet_name_pattern = request.GET.get('pet_name_pattern', None)

    pet_photos = PetPhoto.objects.all()

    if pet_name_pattern:
        pet_photos = pet_photos.filter(pets__name__icontains=pet_name_pattern)

    context = {
        'pet_photos': pet_photos,
        'pet_name_pattern': pet_name_pattern,
    }
    return render(request, template_name="common/home-page.html", context=context)

def like_pet_photo(request, pk):
    #pet_photo = PetPhoto.objects.get(pk=pk, user=request.user)
    #pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo_like = (PhotoLike.objects \
        .filter(pet_photo_id=pk) \
        .first())
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
