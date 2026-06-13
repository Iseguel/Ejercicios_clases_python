from django.contrib import admin
from django.urls import path, include
from miapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView as loginView, LogoutView as logoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('perfil/', views.perfil, name='perfil'),
    path('tareas/', views.tareas, name='tareas'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path('registro/', views.registro, name='registro'),
    # templates/registration/login.html
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('estudiantes/', include('estudiantes.urls')), 
    # LogoutView redirige según LOGOUT_REDIRECT_URL en settings.py
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]