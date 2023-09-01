from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_second.common.urls')),
    path('accounts/', include('petstagram_second.accounts.urls')),
    path('pets/', include('petstagram_second.pets.urls')),
    path('photos/', include('petstagram_second.photos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
