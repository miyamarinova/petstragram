from django.shortcuts import render

# Create your views here.
def create_photo(request):
    context={}
    return render(request, template_name='photos/photo-add-page.html',context=context)

def details_photo(request,pk):
    context={}
    return render(request, template_name='photos/photo-details-page.html',context=context)

def edit_photo(request, pk):
    context={}
    return render(request,template_name='photos/photo-edit-page.html',context=context)