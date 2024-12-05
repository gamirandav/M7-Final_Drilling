from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm


def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar.html', {'laboratorios': laboratorios})


# def agregar_laboratorio(request):
#    if request.method == 'POST':
#        form = LaboratorioForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('listar_laboratorios')
#    else:
#        form = LaboratorioForm()
#    return render(request, 'form.html', {'form': form})


def agregar_laboratorio(request, laboratorio_id=None):
    # Si se proporciona un ID, obtén el laboratorio existente
    laboratorio = get_object_or_404(
        Laboratorio, id=laboratorio_id) if laboratorio_id else None

    if request.method == 'POST':
        # Procesar datos enviados en el formulario
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()  # Guarda el laboratorio
            # Redirigir a la lista de laboratorios
            return redirect('listar_laboratorios')
    else:
        # Mostrar formulario vacío o prellenado para editar
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'form.html', {'form': form, 'laboratorio': laboratorio})


def editar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'form.html', {'form': form})


def eliminar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('listar_laboratorios')
    return render(request, 'eliminar.html', {'laboratorio': laboratorio})
