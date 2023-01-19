from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from clientes.api.serializers import ClientesSerializer
from clientes.api.validadores.validador import valida_cep, valida_cpf
from clientes.models import Clientes


    

class ClienteViewSet(generics.ListAPIView):

    filter_backends = (filters.SearchFilter,)
    search_fields = ('cpf', 'id_cliente', 'nome_completo')
    
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer




class ClienteBViewSet(generics.CreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data_compare = self.request.data
            if valida_cep(data_compare['cep']) and valida_cpf(data_compare['cpf']):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
    
class ClienteUViewSet(generics.RetrieveUpdateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
    
    def put(self, request):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data_compare = self.request.data
            if valida_cep(data_compare['cep']) and valida_cpf(data_compare['cpf']):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    #https://www.django-rest-framework.org/api-guide/routers/
 
    
    
  
   



   
   
        
        
        
        