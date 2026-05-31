from django.shortcuts import render
from .forms import ContactForm, RegistroForm
from .models import Contacto

# Vista de inicio.
# Esta función se ejecuta cuando el usuario entra a la ruta principal "/".
def home(request):
    return render(request, 'miapp/home.html')  # Renderiza el template home.html


# Vista de contacto.
# Esta función se ejecuta cuando el usuario entra a "/contacto/".

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            payload = f"[CONTACTO] name={name}, email={email}, message={message}"
            print(payload, flush=True)

            Contacto.objects.create(
                name=name,
                email=email,
                message=message
            )
            return render(request, 'miapp/contacto.html', {'form': form, 'mensaje': '¡Gracias por contactarnos!'})
    else:
        form = ContactForm()
    
    return render(request, 'miapp/contacto.html', {'form': form})



# Vista de nosotros.
# Esta función se ejecuta cuando el usuario entra a "/nosotros/".
def nosotros(request):
    return render(request, 'miapp/nosotros.html')  # Renderiza el template nosotros.html

def productos(request):
    return render(request, 'miapp/productos.html')

def perfil(request):
    context = {
        'nombre': 'Carlos Ramírez',
        'email': 'carlos.ramirez@example.com',
        'edad': 30,
        'ciudad': 'Santiago',
    }
    return render(request, 'miapp/perfil.html', context)

def tareas(request):
    tareas = [
        {'titulo': 'Estudiar Django', 'completada': True},
        {'titulo': 'Hacer ejercicio', 'completada': False},
        {'titulo': 'Leer documentación', 'completada': False},
        {'titulo': 'Practicar templates', 'completada': False},
    ]
    return render(request, 'miapp/tareas.html', {'tareas': tareas})



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