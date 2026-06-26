from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'loggin/registro.html', {'form': form})



def productos_view(request):
    productos = [
        {'nombre': 'producto_1', 'categoria': 'Cuadros', 'precio': 15990},
        {'nombre': 'producto_5', 'categoria': 'Miniaturas', 'precio': 7990},
        {'nombre': 'producto_8', 'categoria': 'Accesorios', 'precio': 3990},
    ]
    return render(request, 'loggin/productos.html', {'productos': productos})

@login_required  # vista protegida 
def perfil_view(request):
    contexto = {
        'usuario': request.user,
        'session_key': request.session.session_key,
        'session_expiry': request.session.get_expiry_date(),
    }
    return render(request, 'loggin/perfil.html', contexto)