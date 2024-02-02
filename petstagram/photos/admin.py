from django.contrib import admin

from petstagram.photos.models import PetPhoto


# Register your models here.
@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'location', 'created_at', 'short_description', 'tagged_pets')

    def tagged_pets(self, obj):
        return ', '.join(pet.name for pet in obj.pets.all())

    def short_description(self, obj):
        return obj.description[:15]

    def link_to_pet(self,obj):
        return u'<a href="/">%s</a>' % obj.pk

    link_to_pet.allow_tags = True


