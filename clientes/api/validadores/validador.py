import requests
from rest_framework import serializers, status
from rest_framework.response import Response


# consome api:
def valida_cep(cep):
    req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if req.status_code == 200:
        req = req.json()
        try:
            localidade = req['localidade']
            return Response(f'Cep:{cep}, cidade:{localidade}, validado!', status=status.HTTP_200_OK)
        except:
            raise serializers.ValidationError(
                        f'Cep: {cep}, está invalido favor conferir!', code=status.HTTP_400_BAD_REQUEST)
    else:
        raise serializers.ValidationError(
            f'Cep: {cep}, está invalido favor conferir!', code=status.HTTP_400_BAD_REQUEST)


def valida_cpf(documento):
    if len(documento) > 14 or len(documento) < 11 or len(documento) > 11:
        return False
    else:
        val = 0
        for d in range(0, 11):
            val += int(documento[d])
            d += 1
        if int(documento[0]) == val / 11:
            raise serializers.ValidationError(
                                    f'CPF: {documento}, está invalido favor conferir!', code=status.HTTP_400_BAD_REQUEST)
        else:
            soma = 0
            count = 10
            for i in range(0, len(documento)-2):
                soma = soma + (int(documento[i])*count)
                i += 1
                count -= 1
            dg1 = 11-(soma % 11)
            if dg1 >= 10:
                dg1 = 0
# verifica os 11 digit
            soma = 0
            count = 10
            for i in range(1, len(documento)-1):
                soma = soma + (int(documento[i])*count)
                i += 1
                count -= 1
            dg2 = 11-(soma % 11)
            if dg2 >= 10:
                dg2 = 0
            if int(documento[9]) != dg1 or int(documento[10]) != dg2:
                raise serializers.ValidationError(
                                        f'CPF: {documento}, está invalido favor conferir!', code=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(f'Cep:{documento} validado!', status=status.HTTP_200_OK)
