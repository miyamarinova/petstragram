from django.conf.urls.static import static
from django.contrib import admin
from django.core.mail import send_mail
from django.urls import path, include

from petstagram import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('accounts/', include('petstagram.accounts.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('photos/', include('petstagram.photos.urls')),
]

# Show the Uploaded Images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


send_mail(
    subject="It works",
    message="It works without HTML",
    from_email="miyamarinova@gmail.com",
    recipient_list=["kowevo6436@facais.com"],
    html_message="<h1>It works with HTML!</h1>",
    fail_silently=False,
)