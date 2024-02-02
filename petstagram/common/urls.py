from django.conf import settings

from django.urls import path, include
from petstagram.common.views import index
urlpatterns = [
    path('',index, name='index')
]