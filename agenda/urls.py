from django.urls import path
from . import views
 
urlpatterns = [
    path('servicos/', views.servicos_disponiveis),
    path('servicos/criar/', views.criar_servico),
    path('servicos/detalhes/', views.detalhes_servico),
    path('agendamentos/', views.listar_agendamentos),
    path('agendamentos/criar/', views.criar_agendamento),
    path('agendamentos/detalhes/', views.detalhes_agendamento),
]   