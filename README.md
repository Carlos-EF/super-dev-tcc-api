# Super Dev TCC API — Feliks

API REST desenvolvida para dar suporte ao sistema de gestão imobiliária. O backend centraliza operações de cadastro e consulta de imóveis, clientes, corretores e condomínios, além de autenticação, consulta de CEP e armazenamento de imagens.

## Funcionalidades

- **Imóveis:** cadastro, consulta, edição e remoção; filtros, ordenação e paginação; informações específicas de casas, apartamentos e terrenos.
- **Imagens dos imóveis:** envio, consulta e gerenciamento de imagens usando o Supabase Storage. São aceitos arquivos JPEG, PNG e WebP, com limite de 5 MB por imagem.
- **Clientes:** gerenciamento de clientes e dados complementares de clientes interessados.
- **Corretores:** cadastro, consulta, edição, exclusão e listagem para seleção em formulários.
- **Condomínios:** cadastro, consulta, edição, exclusão e consulta de cidades e bairros.
- **Autenticação:** cadastro, login e renovação de sessão via Supabase Auth; identificação do usuário autenticado por token Bearer.
- **Consulta de CEP:** integração com a BrasilAPI.
- **Health check:** endpoint para verificar se a API está respondendo.

## Tecnologias

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) e [Uvicorn](https://www.uvicorn.org/)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) para configurações por variáveis de ambiente
- [SQLAlchemy](https://www.sqlalchemy.org/) e PostgreSQL
- [Supabase Python Client](https://supabase.com/docs/reference/python/introduction) para autenticação e armazenamento de arquivos
- [Requests](https://requests.readthedocs.io/) para integração com a BrasilAPI

## Pré-requisitos

- Python 3.10 ou superior.
- PostgreSQL acessível pela aplicação (pode ser o banco de dados do Supabase).
- Projeto Supabase configurado para autenticação e Storage.
- Git instalado para clonar o repositório.

## Instalação e execução local

### 1. Clonar o repositório

```bash
git clone https://github.com/Carlos-EF/super-dev-tcc-api.git
cd super-dev-tcc-api
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv .venv
```

No Windows, usando PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, no mesmo nível de `requirements.txt`, com os seguintes valores:

```dotenv
DATABASE_URL=postgresql+psycopg://USUARIO:SENHA@HOST:5432/NOME_DO_BANCO
SUPABASE_URL=https://SEU_PROJETO.supabase.co
SUPABASE_KEY=SUA_CHAVE_SUPABASE
SUPABASE_BUCKET=nome-do-bucket
ENVIROMENT=dev
LOG_LEVEL=INFO
```

Substitua os valores de exemplo pelos dados do seu ambiente:

| Variável | Finalidade |
| --- | --- |
| `DATABASE_URL` | URL de conexão PostgreSQL utilizada pelo SQLAlchemy. O projeto inclui o driver `psycopg`. |
| `SUPABASE_URL` | URL do projeto Supabase. |
| `SUPABASE_KEY` | Chave configurada para o acesso do backend ao Supabase. |
| `SUPABASE_BUCKET` | Nome do bucket do Supabase Storage usado para as imagens dos imóveis. |
| `ENVIROMENT` | Ambiente de execução. O valor `prod` desabilita a documentação Swagger; o nome da variável está escrito assim no código. |
| `LOG_LEVEL` | Nível de log da aplicação, por exemplo `INFO` ou `DEBUG`. |

Não compartilhe o `.env` nem faça commit de credenciais. Configure no Supabase as permissões necessárias para autenticação, upload e acesso às imagens.

### 5. Criar as tabelas do banco

Execute o script SQL abaixo **uma vez** no banco PostgreSQL configurado em `DATABASE_URL` (por exemplo, pelo SQL Editor do Supabase):

```text
src/tcc/infrastructure/sql/TCC.sql
```

O script define as tabelas usadas para usuários, clientes, interessados, corretores, condomínios, imóveis, tipos específicos de imóvel e imagens. Verifique se o banco está correto antes de executar, pois o script cria tabelas e não é uma migração automática.

### 6. Configurar o Supabase Storage

Crie no Supabase Storage um bucket com o nome definido em `SUPABASE_BUCKET` e configure as permissões de upload e acesso compatíveis com o seu ambiente. A API gera URLs públicas para as imagens armazenadas, portanto revise a política de acesso do bucket antes de utilizá-lo com dados reais.

### 7. Iniciar a API

Na raiz do repositório, com o ambiente virtual ativado e o `.env` configurado, execute:

```bash
python -m uvicorn tcc.central:app --app-dir src --reload
```

Por padrão, a API ficará disponível em [http://localhost:8000](http://localhost:8000).

## Documentação e verificação

Em ambiente de desenvolvimento (`ENVIROMENT=dev`), a documentação interativa fica disponível em:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- Health check: [http://localhost:8000/health](http://localhost:8000/health)

O endpoint `/health` retorna o estado da API, o ambiente e a informação sobre a habilitação do Swagger. Em ambiente `prod`, os endpoints de documentação são desabilitados.

## Principais grupos de endpoints

| Prefixo | Finalidade |
| --- | --- |
| `/health` | Verificação de disponibilidade da API. |
| `/auth` | Cadastro, login, renovação de sessão e dados do usuário autenticado. |
| `/propertys` | Operações com imóveis, detalhes por tipo e imagens. |
| `/clients` | Operações com clientes e clientes interessados. |
| `/brokers` | Operações com corretores. |
| `/condominiums` | Operações com condomínios, cidades e bairros. |
| `/ceps/{cep}` | Consulta de endereço por CEP na BrasilAPI. |

As rotas de gestão de imóveis, clientes, corretores e condomínios exigem autenticação. Envie o token de acesso do Supabase no cabeçalho HTTP:

```http
Authorization: Bearer SEU_ACCESS_TOKEN
```

Os parâmetros, schemas de request/response e códigos de status de cada rota estão descritos no Swagger UI.

## Estrutura do projeto

```text
src/
└── tcc/
    ├── api/
    │   ├── routes/           # Endpoints REST
    │   ├── schemas/          # Schemas de entrada e saída da API
    │   ├── app.py            # Criação e configuração da aplicação FastAPI
    │   ├── configurations.py # Configurações carregadas do .env
    │   └── dependencies.py   # Dependências, sessão e autenticação
    ├── core/                 # Recursos centrais de autenticação
    ├── infrastructure/
    │   ├── models/           # Modelos SQLAlchemy
    │   ├── services/         # Serviços de autenticação e Storage
    │   ├── sql/              # SQL de estrutura e scripts de seed
    │   └── connection.py     # Conexões com PostgreSQL e Supabase
    ├── repository/           # Consultas e persistência de dados
    └── central.py            # Exporta a aplicação ASGI

main.py                       # Arquivo na raiz do projeto
requirements.txt              # Dependências Python
```

Na inicialização, a aplicação tenta executar o script de seed definido em `src/tcc/infrastructure/sql/scripts/seeds/seed.sql` quando a tabela `clientes` está vazia. Por isso, configure o banco e crie as tabelas antes de iniciar o servidor.

## Integração com o front-end

O front-end Angular correspondente está no repositório [super-dev-tcc-ng](https://github.com/Carlos-EF/super-dev-tcc-ng). Em desenvolvimento, o CORS da API permite a origem `http://localhost:4200`. Caso o front-end seja servido de outra origem, ajuste a configuração de CORS em `src/tcc/api/app.py`.

---

Projeto acadêmico desenvolvido como Trabalho de Conclusão de Curso (TCC).
