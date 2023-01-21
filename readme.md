
# Api_Cadastro com Django Rest Framework


Desenvolvido este repositório para criar um CRUD API Simples com alguns validadores, contendo os recursos GET, POST PUT, PATCH podendo a utilização de pk  e de filtros de nome, CPF.




## Deploy

Para fazer o deploy desse projeto rode


Conexão do servidor ao DB:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'empresa',     -- NOME DO BANCO
        'USER': 'root',        -- USUARIO DO BANCO
        'PASSWORD': '123456',  -- COLOCAR SENHA DO DB
        'HOST': '127.0.0.1',   -- COLOCAR IP CASO NÃO FOR LOCAL
        'PORT': '3306',
    }
}
```


Configuração do ambiente:
```bash
 py -m venv venv
 .\venv\scripts\activate    
 pip install -r requirements.txt
 py manage.py makemigrations clientes
 py manage.py migrate
 py manage.py runserver
```


## Funcionalidades


Caminhos:
- v1/clientes/                   -- CONSULTA TODOS
- v1/clientes/cadastrar/         -- CADASTRA CLIENTES
- v1/clientes/buscar/            -- BUSCA CLIENTES COM FILTRO ?cpf=  ?nome_completo=  ?id_cliente=
- v1/clientes/buscar/<int:pk>    -- BUSCA SOMENTE COM PK
- v1/clientes/alterar/<int:pk>   -- Altera Cliente com pk
- v1/clientes/alterar/           -- Altera com o Filtro
- v1/api/schema/swagger-ui/      -- Documentação Swagger


Extras:
    Adicionado um validador de cpf, caso for testar o cpf colocar um valido recomendo gerar pelo https://www.4devs.com.br/gerador_de_cpf.
    - utiliza-se um calculo para está validação.


## Diario de Desenvolvimento


<p> Dia 19/01 - Começo do projeto (Validadores - Criados e testados)
<p> Dia 20/01 - Adicionado os validadores e ajustado as regras/ criado as views colocados os filtros 
<p> Dia 21/01 - Ajustes de erro de sintaxe dos validadores, revisão e adicionado o Swagger



## Stack utilizada

**Back-end:** PYTHON, DJANGO REST

