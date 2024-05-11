from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto

PET_PHOTOS_DATA = {
        "photo": "photo.jpg",
        "description": "https://example.com/test.jpg",
        "location": "2020-01-01",
    }

def create_valid_pet(user, pets):
    pet = PetPhoto.objects.create(
        **PET_PHOTOS_DATA,
        user=user,
    pets=pets)
    pet.save()
    return pet