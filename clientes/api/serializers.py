import django_filters
import requests
from rest_framework import serializers, status
from rest_framework.response import Response

from clientes.models import Clientes


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        


class Cliente_update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['telefone', 'sexo', 'cep', 'cidade', 'estado', 'logradouro']



class UserUpdateSerialier(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = '__all__'
        read_only_fields = ("id_cliente", "cpf")

