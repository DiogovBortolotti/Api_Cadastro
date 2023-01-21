from django.urls import path

from clientes.api.viewsets import (ClienteAtualizarViewCliente,
                                   ClienteAtualizarViewClienteFiltro,
                                   ClienteViewBuscar, ClienteViewBuscarFiltro,
                                   ClienteViewCriar, ClienteViewSet)

urlpatterns = [

    path('clientes/', ClienteViewSet.as_view()), 
    path('clientes/cadastrar/', ClienteViewCriar.as_view()), 
    path('clientes/buscar/', ClienteViewBuscarFiltro.as_view()), 
    path('clientes/buscar/<int:pk>', ClienteViewBuscar.as_view()), 
    path('clientes/alterar/', ClienteAtualizarViewCliente.as_view()), 
    path('clientes/alterar/<int:pk>', ClienteAtualizarViewCliente.as_view()), 

    path('clientes/buscare/', ClienteAtualizarViewClienteFiltro.as_view()), 
    path('clientes/buscare/<int:pk>', ClienteAtualizarViewClienteFiltro.as_view()),

 
]


