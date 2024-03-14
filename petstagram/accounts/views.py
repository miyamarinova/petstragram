from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm
from petstagram.accounts.models import PetstagramUser, Profile


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'

class SignUpUserViews(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result

def signout_user(request):
    logout(request)
    return redirect('index')

class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all.prefetch_related("user").all()
    template_name = 'accounts/details_profile.html'

def edit_profile(request, pk):
    context = {

    }
    return render(request, template_name="accounts/edit_profile.html", context=context)


def delete_profile(request, pk):
    context = {

    }
    return render(request, template_name="accounts/delete_profile.html", context=context)
