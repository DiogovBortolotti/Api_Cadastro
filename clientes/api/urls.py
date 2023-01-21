from django.urls import path

from clientes.api.viewsets import (ClienteBViewSet, ClienteUViewSet,
                                   ClienteViewSet, ListUpdateAPIView)

urlpatterns = [
    path('clientes/', ClienteViewSet.as_view()), 
    #path('clientes/(?P<cpf>([a-z0-9-])+)$', ClienteViewSet.as_view()), 
    path('clientes/<int:pk>', ClienteViewSet.as_view()), 
    path('clientes/cadastro/', ClienteBViewSet.as_view()), 
    path('clientes/cadastro/atualizar/<int:pk>', ClienteUViewSet.as_view()),
    path('clientes/cadastro/testeatualiza/', ListUpdateAPIView.as_view()),
    path('clientes/cadastro/testeatualiza/<int:pk>', ListUpdateAPIView.as_view()),
    #path('clientes/cadastro/testeatualiza/^(?P<cpf>.*)/$', ClienteUViewSet.as_view())#tem que colocar o pk para procurar pelo cpf id e nome
    #path('clientes/cadastro/?search=/atualizar', ClienteUViewSet.as_view()),
]


