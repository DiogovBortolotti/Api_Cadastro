from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from clientes.api.serializers import (Cliente_update_Serializer,
                                      ClientesSerializer)
from clientes.api.validadores.validador import valida_cep, valida_cpf
from clientes.models import Clientes


class ClienteViewSet(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpf', 'id_cliente', 'nome_completo']

    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer





class ClienteBViewSet(generics.CreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data_compare = self.request.data
            if valida_cep(data_compare['cep'], data_compare['cidade'], data_compare['estado']) and valida_cpf(data_compare['cpf']):
                if Clientes.objects.filter(cpf=data_compare['cpf']).exists():
                    raise serializers.ValidationError('CPF já cadastrado')
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
            
            
#RetrieveUpdateAPIView
#generics.ListAPIView
#RetrieveUpdateDestroyAPIView -- aki funciona
 
 
 #deu problema aki --- olhar amanha - Fonte: Não salva o update devido o filtro e o listapiview
class ClienteUViewSet(generics.ListAPIView, generics.RetrieveUpdateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpf', 'id_cliente', 'nome_completo']
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


   #ISOLEI SOMENTE PARA TRAZER STATUS -- MAS TEM QUE AJUSTAR
    def put(self, request):
        sales = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(instance=sales, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
  

#Fica duplicando 
  #  def patch(self, request, *args, **kwargs): 
   #     serializer = ClientesSerializer(data=request.data)
   #     if serializer.is_valid(raise_exception=True):
   #         data_compare = self.request.data
   #         if valida_cep(data_compare['cep'], data_compare['cidade'], data_compare['estado']) and valida_cpf(data_compare['cpf']):
   #             
   #             #if Clientes.objects.filter(cpf=data_compare['cpf']).exists():
    #            #    raise serializers.ValidationError('CPF já cadastrado')
    #            serializer.save()
    #            return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    else:
     #       return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        