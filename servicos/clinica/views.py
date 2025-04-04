from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Medico, Consulta
from .form import ConsultaForm

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'listar_medicos': medicos} )

def criar_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save()
        return redirect('detalhes_consulta', id=consulta.id)
    else:
        form = ConsultaForm()

    return render(request, 'clinica/form_consulta.html', {'form': form})

def detalhes_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    return render(request, 'clinica/detalhes_consulta.html', {'consulta': consulta})




# Create your views here.
