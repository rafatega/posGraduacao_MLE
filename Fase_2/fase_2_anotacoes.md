- [Fase 2 - Big Data Architecture](#fase-2---big-data-architecture)
  - [Banco de Dados Relacional (SQL)](#banco-de-dados-relacional-sql)
    - [Cadeias de comandos](#cadeias-de-comandos)
      - [DDL (Data Definition Language)](#ddl-data-definition-language)
      - [DML (Data Manipulation Language)](#dml-data-manipulation-language)
      - [DCL (Data Control Language)](#dcl-data-control-language)
      - [TCL (Transaction Control Language)](#tcl-transaction-control-language)
    - [Docker](#docker)
      - [Criando com um contâiner com PostgreSQL](#criando-com-um-contâiner-com-postgresql)
      - [Criando um contâiner com MongoDB](#criando-um-contâiner-com-mongodb)
  - [Big Data Structures](#big-data-structures)
    - [Data Werehouse (RedShift, BigQuery e SQL Data Warehouse)](#data-werehouse-redshift-bigquery-e-sql-data-warehouse)
      - [OLTP (Online Transaction Processing)](#oltp-online-transaction-processing)
      - [OLAP (Online Analytical Processing)](#olap-online-analytical-processing)
      - [RedShift](#redshift)


# Fase 2 - Big Data Architecture

## Banco de Dados Relacional (SQL)
- **Definição**: Bancos de dados relacionais armazenam dados em tabelas estruturadas com linhas e colunas, utilizando SQL (Structured Query Language) para manipulação e consulta dos dados.

### Cadeias de comandos
![Cadeias de Comandos SQL](../app/Imagens/sqlCommands.png)

#### DDL (Data Definition Language)
- **CREATE**: Cria novas tabelas ou bancos de dados.
- **ALTER**: Modifica a estrutura de tabelas existentes.
- **DROP**: Remove tabelas ou bancos de dados existentes.
- **RENAME**: Renomeia tabelas ou colunas.
- **TRUNCATE**: Remove todos os registros de uma tabela, mas mantém a estrutura da tabela.
- **COMMENT**: Adiciona comentários a tabelas ou colunas.

#### DML (Data Manipulation Language)
- **SELECT**: Recupera dados de uma ou mais tabelas.
- **INSERT**: Adiciona novos registros a uma tabela.
- **UPDATE**: Modifica registros existentes em uma tabela.
- **DELETE**: Remove registros de uma tabela.
- **MERGE**: Combina dados de duas tabelas com base em uma condição especificada.
- **CALL**: Executa procedimentos armazenados no banco de dados.
- **EXPLAIN PLAN**: Fornece informações sobre como o banco de dados executará uma consulta SQL.
- **LOCK TABLE**: Bloqueia uma tabela para evitar acesso concorrente durante operações críticas

#### DCL (Data Control Language)
- **GRANT**: Concede permissões a usuários ou roles para acessar ou manipular objetos do banco de dados.
- **REVOKE**: Remove permissões concedidas anteriormente a usuários ou roles.

#### TCL (Transaction Control Language)
- **COMMIT**: Salva todas as alterações feitas na transação atual.
- **ROLLBACK**: Desfaz todas as alterações feitas na transação atual.
- **SAVEPOINT**: Define um ponto intermediário dentro de uma transação para permitir rollback parcial.
- **SET TRANSACTION**: Configura propriedades da transação atual, como o nível de isolamento.

### Docker
- **Definição**: Docker é uma plataforma de código aberto que automatiza a implantação de aplicativos dentro de contêineres leves e portáteis.

#### Criando com um contâiner com PostgreSQL
- Para fazer o docker conversar via network:
```bash
docker network create --driver bridge minha-rede
```
Hash gerada: `409edcff53bc6dd9c78b1f5b27dd4ce75973fb5ddd71b26ed2a471c61ef0dec6`
Para conferir a rede:
```bash
docker network ls
```
- Comando para criar o contâiner com PostgreSQL:
```bash
docker run -d \
--name meu-postgres \
--network minha-rede \
-e POSTGRES_USER=ta \
-e POSTGRES_PASSWORD=102030 \
-e POSTGRES_DB=db_fiap \
-p 5433:5432 \
postgres:latest
```
Isso gerou a hash do contâiner: `7a124504d3b71805e0e94f6f6054a0ac8b184a4a1305addabaa30f20b624da4c`

- Para parar o contâiner:
```bash
docker stop 7a12
```
- Criando a imagem do PGADMIN:
```bash
docker run \
--name my-pgadmin \
--network=minha-rede \
-p 15432:80 \
-e PGADMIN_DEFAULT_EMAIL=rafael_tegazzini@hotmail.com \
-e PGADMIN_DEFAULT_PASSWORD=postgre \
-d dpage/pgadmin4
```

#### Criando um contâiner com MongoDB
- Comando para criar o contâiner com MongoDB:
```bash
docker run -d --name mongodb -p 27017:27017 mongo:7
```
- Comando para ver se está rodando:
```bash
docker ps
```

## Big Data Structures

### Data Werehouse (RedShift, BigQuery e SQL Data Warehouse)

![Ciclo dos Dados](C:/Users/Tega/Documents/Projetos/posGraduacao_MLE/app/Imagens/cicloDosDados.png)

#### OLTP (Online Transaction Processing)
- **Definição**: OLTP é um sistema de processamento de transações online que é projetado para gerenciar grandes volumes de transações em tempo real, como vendas, reservas e operações bancárias. Ele é otimizado para operações de leitura e escrita rápidas, garantindo a integridade dos dados e a consistência durante as transações. Bastante usado para escritas.

#### OLAP (Online Analytical Processing)
- **Definição**: OLAP é um sistema de processamento analítico online que é projetado para consultas complexas e análise de grandes volumes de dados. Ele é otimizado para operações de leitura intensiva, permitindo que os usuários realizem análises multidimensionais, como agregações, drill-down e slice-and-dice, para obter insights estratégicos a partir dos dados armazenados. Bastante usado para leituras, agregações médias.

#### RedShift
- **Definição**: RedShift é um serviço de data warehousing em nuvem da Amazon Web Services (AWS) que permite armazenar e analisar grandes volumes de dados usando SQL. Ele é projetado para ser escalável, rápido e fácil de usar, oferecendo recursos como armazenamento em colunas, compressão de dados e otimização de consultas para melhorar o desempenho das análises. RedShift é amplamente utilizado para análise de dados empresariais, relatórios e inteligência de negócios.