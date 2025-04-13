# portfolio_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('django-admin/', admin.site.urls),  # Admin Django standard
    path('', include('jeux.urls')),  # Notre application portfolio
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Ajouter les URLs pour les fichiers média en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()