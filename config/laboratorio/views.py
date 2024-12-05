from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm


def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar.html', {'laboratorios': laboratorios})


def agregar_laboratorio(request, laboratorio_id=None):

    laboratorio = get_object_or_404(
        Laboratorio, id=laboratorio_id) if laboratorio_id else None

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
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
