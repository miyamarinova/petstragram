from django.urls import path, include
from petstagram.accounts.views import SignUpUserViews, SignInUserView,ProfileDetailsView,signout_user, ProfileDeleteView, ProfileUpdateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', SignUpUserViews.as_view(), name='signup user'),
    path('signin/', SignInUserView.as_view(), name='signin user'),
    path('logout/', signout_user, name='logout'),

    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details profile'),
        path('edit/',ProfileUpdateView.as_view() , name='profile edit'),
        path('delete/',ProfileDeleteView.as_view(), name='delete profile')
            ]),
         ),
]