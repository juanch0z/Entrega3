
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.Marketpets.urls')),
    path('apps.api/version1',include('apps.api.urls')),
    path('docs/',include_docs_urls(title='Documentacion de api'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)