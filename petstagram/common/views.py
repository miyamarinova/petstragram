
from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import PhotoLike
from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from django.views import generic as views

class IndexView(views.ListView):
    model = PetPhoto
    template_name = "common/home-page.html"
    paginate_by = 2

    @property
    def pet_name_pattern(self):
        return self.request.GET.get("pet_name_pattern", None)

    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            pet_name = search_form.cleaned_data.get('pet_name')
            if pet_name:
                queryset = queryset.filter(tagged_pets__name__icontains=pet_name)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_name_pattern"] = self.pet_name_pattern or ""
        context['search_form'] = SearchForm(self.request.GET)
        context['comment_form'] = CommentForm()
        return context
    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern
        filter_query = {}

        if pet_name_pattern:
            filter_query['pets__name__icontains'] = pet_name_pattern
        return queryset.filter(**filter_query)

def like_pet_photo(request, photo_id):
    photo = PetPhoto.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = PhotoLike(to_photo=photo, user=request.user)
        like.save()
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = PetPhoto.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def share_pet_photo(request, pk):
    # create link to be copied
    copy(request.META['HTTP_HOST'] + resolve_url('details_photo', pet_photo_id=pk))
