from django.urls import path, include
from petstagram.accounts.views import signup_user,logout, signin_user,details_profile, delete_profile, edit_profile
urlpatterns = [
    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('logout/', logout, name='logout'),

    path('profile/<int:pk>/', include([
        path('', details_profile, name='details profile'),
        path('edit/', edit_profile, name='profile edit'),
        path('delete/', delete_profile, name='delete profile')
            ]),
         ),
]