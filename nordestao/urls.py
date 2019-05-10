from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', include('campeonatos.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('exemplo/', TemplateView.as_view(template_name='frontend/index.html'))
]
