from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('', include('campeonatos.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
