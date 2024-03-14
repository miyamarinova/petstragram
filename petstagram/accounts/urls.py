from django.urls import path, include
from petstagram.accounts.views import SignUpUserViews, SignInUserView,ProfileDetailsView,signout_user, delete_profile, edit_profile
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', SignUpUserViews.as_view(), name='signup user'),
    path('signin/', SignInUserView.as_view(), name='signin user'),
    path('logout/', signout_user, name='logout'),

    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details profile'),
        path('edit/', edit_profile, name='profile edit'),
        path('delete/', delete_profile, name='delete profile')
            ]),
         ),
]