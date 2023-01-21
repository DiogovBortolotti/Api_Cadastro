
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (filters, generics, mixins, serializers, status,
                            viewsets)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from clientes.api.serializers import ClientesSerializer
from clientes.api.validadores.validador import valida_cep, valida_cpf
from clientes.models import Clientes


#Consulta tudo
class ClienteViewSet(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpf', 'id_cliente', 'nome_completo']
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


#Cria conforme a regra
class ClienteViewCriar(generics.CreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpf', 'id_cliente', 'nome_completo']
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




#busca pelo filtro
class ClienteViewBuscarFiltro(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpf', 'id_cliente', 'nome_completo']
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


    
class ClienteViewBuscar(generics.RetrieveAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_cliente','cpf', 'nome_completo']
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

#tudo ok procura pelo id e atualiza
  #RetrieveUpdateDestroyAPIView - ook aki ta realizando
  #RetrieveUpdateAPIView o certo
class ClienteAtualizarViewCliente(generics.RetrieveUpdateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

    
    def patch(self, request,  pk):
        clientes = Clientes.objects.get(id_cliente=pk)
        serializer = ClientesSerializer(instance=clientes, data=request.data,  partial=True)
        print(request.data, pk) # obs propria >> fiquei trancado aki devido como fazer -- aprendi a depurar com print  tem que colocar {}no response para poder ver e trazer os dados hr travadas 5hrs
        if serializer.is_valid():
            data_compare = self.request.data
            if valida_cep(data_compare['cep'], data_compare['cidade'], data_compare['estado']):
                serializer.save()

        return Response(serializer.data) 


    
    def put(self, request,  pk):
        clientes = Clientes.objects.get(id_cliente=pk)
        serializer = ClientesSerializer(instance=clientes, data=request.data,  partial=True)
        print(request.data, pk) 
        if serializer.is_valid():
            data_compare = self.request.data
            if valida_cep(data_compare['cep'], data_compare['cidade'], data_compare['estado']):
                serializer.save()

        return Response(serializer.data)







#procura o filtros e lista generics.UpdateAPIView,generics.ListAPIView
class ClienteAtualizarViewClienteFiltro(generics.UpdateAPIView,generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_cliente','cpf', 'nome_completo']
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
    
    
    def put(self, request,  pk):
        clientes = Clientes.objects.get(cpf=pk)
        serializer = ClientesSerializer(instance=clientes, data=request.data,  partial=True)
        print(request.data, pk) 
        if serializer.is_valid():
            data_compare = self.request.data
            if valida_cep(data_compare['cep'], data_compare['cidade'], data_compare['estado']):
                serializer.save()

        return Response(serializer.data) 


    def patch(self, request,  pk):
        clientes = Clientes.objects.get(id_cliente=pk)
        serializer = ClientesSerializer(instance=clientes, data=request.data,  partial=True)
        print(request.data, pk) 
        if serializer.is_valid():
            data_compare = self.request.data
            if valida_cep(data_compare['cep'], data_compare['cidade'], data_compare['estado']):
                serializer.save()

        return Response(serializer.data) 





