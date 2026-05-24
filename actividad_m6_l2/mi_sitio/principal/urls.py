# blog/urls.py
from django.urls import path
from . import views  # importa las views de esta misma app

urlpatterns = [
    path('', views.home, name='home'),

      # URL para la página de inicio
]