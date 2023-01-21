#Progresso...


[Diario de Deploy:]
>Documentacao > pendente

>> Dia 19/01 - Started Project (Validadores - Criados e testados)
>> Dia 20/01 - Adicionado os validadores e ajustado as regras/ criado as views colocados os filtros 
>> Dia 21/01 - Encontrado bug na revisão do update -- o Filtro não habilitando o pk para alteração em relação ao filtro de cpf nome.


Caminhos:
v1/clientes/                   -- CONSULTA TODOS
v1/clientes/cadastrar/         -- CADASTRA CLIENTES
v1/clientes/buscar/            -- BUSCA CLIENTES COM FILTRO ?cpf=  ?nome_completo=  ?id_cliente=  
v1/clientes/buscar/<int:pk>    -- BUSCA SOMENTE COM PK
v1/clientes/alterar/<int:pk>   -- Altera Cliente com pk
v1/clientes/buscare/           -- BUG NO FILTRO PARA ALTERAR
v1/clientes/buscare/<int:pk>   -- BUG NO FILTRO PARA ALTERAR
v1/api/schema/swagger-ui/      -- Documentação Swagger





