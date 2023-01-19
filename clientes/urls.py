from django.urls import path

from clientes.api.viewsets import (ClienteBViewSet, ClienteUViewSet,
                                   ClienteViewSet)

urlpatterns = [
    path('cliente/', ClienteViewSet.as_view()), 
    path('cadastrar_cliente/', ClienteBViewSet.as_view()), 
    path('atualizar_cliente/<int:pk>', ClienteUViewSet.as_view()), 
]
