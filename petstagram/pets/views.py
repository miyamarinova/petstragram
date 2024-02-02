from django.shortcuts import render

# Create your views here.
def create_pet(request):
    context={}
    return render(request,template_name='pets/pet-add-page.html',context=context)

def details_pet(request, username, pet_slug):
    context={}
    return render(request,template_name='pets/pet-details-page.html',context=context)

def edit_pet(request, username, pet_slug):
    context = {}
    return render(request,template_name='pets/pet-edit-page.html',context=context)
def delete_pet(request, username, pet_slug):
    context={}
    return render(request,template_name='pets/pet-delete-page.html',context=context)