from django.shortcuts import render
from .models import Servico, Agendamento
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def servicos_disponiveis(request):
    listar_servicos = Servico.objects.all()
    serializer = ServicoSerializer(listar_servicos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_servico(request):
    if request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detalhes_servico(request, pk):
    try:
        servico = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServicoSerializer(servico)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def listar_agendamentos(request):
    listar_agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer( listar_agendamentos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def criar_agendamento(request):
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def detalhes_agendamento(request, pk):
    try:
        agendamento = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data, status=status.HTTP_200_OK)

