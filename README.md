# Desafio CRUD CIT

## 1. Estrutura do Projeto e Arquivos

O projeto está estruturado em módulos Python que se comunicam entre si para implementar um sistema CRUD utilizando PostgreSQL. Os principais arquivos são:

- **`bd.py`**: Gerencia conexão e operações no banco de dados.
- **`pontoescavacao.py`**: Define a classe `PontoEscavacao`.
- **`responsavel.py`**: Define a classe `Responsavel`.
- **`menuponto.py`**: Interface de linha de comando para gerenciar pontos de escavação.
- **`menuresp.py`**: Interface de linha de comando para gerenciar responsáveis.
- **`principal.py`**: Ponto de entrada do sistema, exibindo o menu principal.

## 2. Banco de Dados e Funções CRUD

O banco de dados PostgreSQL armazena informações sobre pontos de escavação e responsáveis.

### Tabelas

- **`responsavel`** (`id`, `nome`, `telefone`, `instituicao`, `especialidade`)
- **`pontos_escavacao`** (`id`, `tipo_ponto`, `latitude`, `longitude`, `altitude`, `descricao`, `data_catalogacao`, `id_responsavel`)

### Funções principais em `bd.py`

- `conectar()` e `fecharconex()` - Gerenciam a conexão com o banco de dados.
- `inserirponto()` e `cadastrar_responsavel()` - Inserem registros no banco.
- `listarponto()` e `listar_responsavel()` - Exibem registros com filtros opcionais.
- `apagarponto()` e `apagarpontos()` - Removem pontos.
- `apagarpontos()` - Exclui todos os registros de pontos.
- `apagarponto(id)` - Remove um ponto específico.
- `atualizaponto()` e `atualizar_responsaveis()` - Alteram registros existentes.

## 3. Interface do Usuário

Os módulos `menuponto.py` e `menuresp.py` contêm menus para interação com o usuário.

### Menu de Pontos de Escavação

1. Listar todos os pontos
2. Inserir um ponto
3. Excluir um ponto ou todos
4. Alterar um ponto
5. Buscar por responsável
0. Voltar ao menu principal

### Menu de Responsáveis

1. Listar todos os responsáveis
2. Inserir um responsável
3. Excluir um responsável ou todos
4. Alterar um responsável
0. Voltar ao menu principal

## 4. Configuração e Execução

### Requisitos

- Python 3.10+
- PostgreSQL instalado e em execução
- Biblioteca `psycopg2` instalada

### Passos para executar

1. Criar o banco de dados `escavacoes` no PostgreSQL.
2. Criar as tabelas `responsavel` e `pontos_escavacao`.
3. Configurar credenciais de conexão no `bd.py`.
4. Executar `python principal.py` para iniciar o sistema.

### Fluxo de Interação

1. O usuário escolhe entre gerenciar pontos de escavação ou responsáveis.
2. Dentro do submenu, escolhe entre listar, inserir, excluir ou alterar registros.
3. O programa coleta os dados e chama a função correspondente em `bd.py`.
4. O banco de dados executa a ação e retorna o resultado.
5. O menu reaparece para nova interação ou encerramento.

## Conclusão

O sistema implementa um CRUD funcional com PostgreSQL, permitindo gerenciar pontos de escavação e responsáveis via linha de comando. Algumas melhorias podem ser feitas para maior segurança e eficiência do sistema.
