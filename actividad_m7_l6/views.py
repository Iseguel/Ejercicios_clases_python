from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Libro


# ============================================================
# READ
# ============================================================

@login_required
def lista_libros(request):
    
    libros = Libro.objects.filter(creado_por=request.user)
    return render(request, 'libros/lista.html', {'libros': libros})


@login_required
def detalle_libro(request, id):
 
    libro = get_object_or_404(Libro, id=id, creado_por=request.user)
    return render(request, 'libros/detalle.html', {'libro': libro})


# ============================================================
# CREATE / UPDATE
# ============================================================

@login_required
def crear_libro(request):
   if request.method == 'POST':
      tipo = request.POST['tipo']
      titulo = request.POST['titulo']
      descripcion = request.POST['descripcion']

      Libro.objects.create(
         creado_por=request.user,
         tipo=tipo,
         titulo=titulo,
         descripcion=descripcion,
      )
      messages.success(
            request,
            'Libro creado correctamente.'
        )
      return redirect('libros:lista')
   return render(request, 'libros/form.html')

@login_required
def editar_libro(request, id):
   libro = get_object_or_404(Libro, id=id, creado_por=request.user)
   #si es un POST
   if request.method == 'POST':  
      libro.tipo = request.POST['tipo']
      libro.titulo = request.POST['titulo']
      libro.descripcion = request.POST['descripcion']
      libro.save()
      return redirect('libros:detalle', id=libro.id)
   else: #si es un GET
      return render(request, 'libros/form.html', {'libro': libro}) 

# ============================================================
#  DELETE + PANEL BIBLIOTECARIO
# ============================================================

@login_required
def eliminar_libro(request, id):
   libro = get_object_or_404(Libro, id=id, creado_por=request.user)

   if request.method == 'POST':
      libro.delete()
      return redirect('libros:lista')
   else:
      return render(request, 'libros/confirmar_eliminar.html', {'libro': libro})


@login_required
@permission_required('libros.change_libro', raise_exception=True)
def panel_libros(request):
   
   libros = Libro.objects.all()
   if request.method == 'POST':
      libro_id = request.POST['libro_id']
      nuevo_estado = request.POST['estado']
      libro = get_object_or_404(Libro, id=libro_id)
      libro.estado = nuevo_estado
      libro.save()
      return redirect('libros:panel')
   else:
      return render(request, 'libros/panel.html', {'libros': libros})   
