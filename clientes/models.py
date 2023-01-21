
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

SEXO = (
    ("M", "Masculino"),
    ("F", "Feminino")
)

UF =(
    ("AC", "AC"),
    ("AL", "AL"),
    ("AM", "AM"),
    ("AP","AP"),
    ("BA","BA"),
    ("CE","CE"),
    ("DF", "DF"),
    ("ES","ES"),
    ("GO","GO"),
    ("MA","MA"),
    ("MG","MG"),
    ("MS","MS"),
    ("MT","MT"),
    ("PA", "PA"),
    ("PB", "PB"),
    ("PE","PE"),
    ("PI","PI"),
    ("PR","PR"),
    ("RJ","RJ"),
    ("RN","RN"),
    ("RO","RO"),
    ("RR","RR"),
    ("RS","RS"),
    ("SC","SC"),
    ("SE","SE"),
    ("SP","SP"),
    ("TO","TO")
)

class Clientes(models.Model):
    id_cliente = models.BigAutoField(
        primary_key=True, auto_created=True)
    nome_completo = models.CharField(max_length=360)
    cpf_regex = RegexValidator(
        regex=r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})") #Exemplos 00000000000, 00000000000000, 000.000.000-00, 00.000.000/0000-00, 000000000-00 ou 00000000/0000-00
    cpf = models.CharField(validators=[cpf_regex], max_length=11) # obs:-- não habilitado o unique=True, pois estava dando conflito com a regra do path informando que ja havia, criado regra de get cpf caso ja tenha ele impedir
    telefone_regex = RegexValidator(regex=r"\d{11}")  # Exemplos válidos: [00]0000-0000
    telefone = models.CharField(
        validators=[telefone_regex], max_length=11)
    sexo = models.CharField(
        max_length=1, choices=SEXO, blank=False, null=False)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=250)
    estado = models.CharField(
        max_length=2, choices=UF, blank=False, null=False)
    logradouro = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.nome_completo


#regex montados e validados: https://regex101.com/