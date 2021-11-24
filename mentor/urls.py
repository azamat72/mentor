from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('backend.routes'))
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


