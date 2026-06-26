from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='loggin/login.html',
        authentication_form=LoginForm,
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('productos/', views.productos_view, name='productos'),
    path('perfil/', views.perfil_view, name='perfil'),
]