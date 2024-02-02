from django.http import HttpResponse
from django.shortcuts import render, redirect
from petstagram.common.views import index
# Create your views here.
# Callables:
# - all functions
# - objects with overriden __call__ method

def signup_user(request):
    context = {

    }
    return render(request, template_name="accounts/signup_user.html", context=context)


def signin_user(request):
    context = {

    }
    return render(request, template_name="accounts/signin_user.html", context=context)

def logout(request):
    return redirect("index")


def details_profile(request, pk):
    context = {

    }
    return render(request, template_name="accounts/details_profile.html", context=context)

def edit_profile(request, pk):
    context = {

    }
    return render(request, template_name="accounts/edit_profile.html", context=context)


def delete_profile(request, pk):
    context = {

    }
    return render(request, template_name="accounts/delete_profile.html", context=context)
