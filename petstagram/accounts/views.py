from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy, reverse
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
    queryset = Profile.objects.prefetch_related("user").all()
    template_name = 'accounts/details_profile.html'

class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    def get_success_url(self):
        return reverse('details profile', kwargs={
            "pk": self.object.pk,
        })
    fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['date_of_birth'].widget.attrs['type'] = 'date'
        return form

class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/delete_profile.html"
    fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture')



