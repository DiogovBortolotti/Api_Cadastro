from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

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
    
    #Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    #Documentação do projeto
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
 
]


