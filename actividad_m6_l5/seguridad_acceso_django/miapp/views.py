from django.shortcuts import render
from .forms import ContactForm, RegistroForm
from .models import Contacto
import logging
from django.contrib.auth.decorators import permission_required, login_required

@login_required
@permission_required('miapp.view_contacto', raise_exception=True)
def contacto(request):

    # Consultar todos los contactos para mostrarlos en el template
    contactos = Contacto.objects.all()

    if request.method == 'POST':

        # Solo procesar el POST si tiene permiso de agregar
        if not request.user.has_perm('miapp.add_contacto'):
            return render(request, 'miapp/contacto.html', {
                'form': ContactForm(),
                'contactos': contactos,
                'error': 'No tienes permisos para enviar contactos.'
            })

        form = ContactForm(request.POST)
        if form.is_valid():
            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            message = form.cleaned_data['message']

            Contacto.objects.create(name=name, email=email, message=message)

            # Paso 2.3 — Recargar contactos después de crear uno nuevo
            contactos = Contacto.objects.all()

            return render(request, 'miapp/contacto.html', {
                'form': ContactForm(),       # form limpio tras envío exitoso
                'contactos': contactos,
                'mensaje': '¡Gracias por contactarnos!'
            })
    else:
        form = ContactForm()

    # Paso 2.3 — Pasar contactos al contexto en GET
    return render(request, 'miapp/contacto.html', {
        'form': form,
        'contactos': contactos,
    })



def productos(request):
    return render(request, 'miapp/productos.html')

# Vista de nosotros.
# Esta función se ejecuta cuando el usuario entra a "/nosotros/".
def nosotros(request):
    return render(request, 'miapp/nosotros.html')  # Renderiza el template nosotros.html

@login_required
def perfil(request):
    context = {
        'nombre': 'Carlos Ramírez',
        'email': 'carlos.ramirez@example.com',
        'edad': 30,
        'ciudad': 'Santiago',
    }
    return render(request, 'miapp/perfil.html', context)

@login_required
def tareas(request):
    tareas = [
        {'titulo': 'Estudiar Django', 'completada': True},
        {'titulo': 'Hacer ejercicio', 'completada': False},
        {'titulo': 'Leer documentación', 'completada': False},
        {'titulo': 'Practicar templates', 'completada': False},
    ]
    return render(request, 'miapp/tareas.html', {'tareas': tareas})

def presentacion(request):
    context = {
        'nombre': 'Ismael Seguel A.',
        'email': 'seguel.ismael@gmail.com',
        'edad': 36,
        'ciudad': 'Santiago',
        'Descripcion': 'Soy un desarrollador apasionado por la tecnología y el aprendizaje continuo. Me encanta explorar nuevas herramientas y frameworks para mejorar mis habilidades y crear proyectos innovadores. En mi tiempo libre, disfruto de la música, el cine y los videojuegos.'
    }
    return render(request, 'miapp/presentacion.html', context)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()           # guarda en BD
            return render(request, 'miapp/registro.html', {
                'form': RegistroForm(),  # form limpio
                'mensaje': '¡Usuario registrado correctamente!'
            })
    else:
        form = RegistroForm()     # form vacío
    return render(request, 'miapp/registro.html', {'form': form})


# Vista de inicio.
# Esta función se ejecuta cuando el usuario entra a la ruta principal "/".
def home(request):
    return render(request, 'miapp/home.html')  # Renderiza el template home.html
