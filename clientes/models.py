import uuid

from django.core.validators import RegexValidator
from django.db import models

# ID
# NOME COMPLETO
# CPF
# TELEFONE
# SEXO
# CEP
# CIDADE
# ESTADO
# LOGRADOURO

# ocorreu erro de migração usar somente o app quando quiser usar migrations (name)
SEXO_CHOICES = (
    ("M", "Masculino"),
    ("F", "Feminino")
)


class Clientes(models.Model):
    id_cliente = models.BigAutoField(
        primary_key=True, auto_created=True, editable=False, serialize=False)
    nome_completo = models.CharField(max_length=360)
    cpf_regex = RegexValidator(
        regex=r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
    cpf = models.CharField(validators=[cpf_regex], max_length=11, unique=True)
    telefone_regex = RegexValidator(regex=r"^\+?1?\d{8,11}$")
    telefone = models.CharField(
        validators=[telefone_regex], max_length=11)
    sexo = models.CharField(
        max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    # Validar no serializer com validadores
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=250)
    estado = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=250)

    def __str__(self):
        return self.nome_completo
