from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .forms import RegistroEstudianteForm


def registro(request):
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo = Group.objects.get(name='estudiante')
            user.groups.add(grupo)
            return redirect('login')
    else:
        form = RegistroEstudianteForm()
    return render(request, 'estudiantes/registro.html', {'form': form})


def lista(request):
    User = get_user_model()
    usuarios = User.objects.all()
    return render(request, 'estudiantes/lista.html', {'usuarios': usuarios})