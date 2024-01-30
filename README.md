# Notlar

Notlar é um sistema distribuído para a gestão de notas de texto.

O objetivo é permitir que os utilizadores guardem, acedam
e recuperem notas de texto em servidores distribuídos, potencialmente localizados em diferentes partes do mundo.

-> [Enunciado](/doc/Notlar%20Enunciado.pdf)

## Especificações

### ⌈ Linguagem utilizada
Python

### ⎮ Arquitetura

Para a realização do projeto foi escolhia a arquiterura de 3 camadas pelo facto de fazer uma separação clara das responsabilidades do sistema e por facilitar a manutenção.

* __Camada de Apresentação__: Responsável por receber comandos do usuário via linha de comando. Envia comandos para a camada de lógica de negócios para processamento. Apresenta resultados e mensagens ao usuário na linha de comando.

* __Camada de Lógica de Negócios__: Contém a lógica principal do sistema. É responsável pela autenticação do usuário, criptografia de notas e distribuição eficiente. É composto por um servidor.
Recebe comandos da camada de apresentação e processa operações correspondentes. Utiliza o protocolo HTTP para operações síncronas, ou seja, operações CRUD (Create, Read, Update, Delete) e interações diretas do usuário.

* __Camada de Dados__: Utiliza o MongoDB como banco de dados para armazenar notas de texto. Implementa mecanismos de persistência eficiente e recuperação de falhas usando as capacidades do MongoDB.

### ⎮ Mecanismo de Nomeação e Localização
Adoção de um sistema de UUIDs (Identificadores Únicos Universais) para cada nota com recurso ao MongoDB para armazenar os documentos de notas, associando cada nota ao identificador, facilitando a localização e referência.

A camada lógica de negócios utiliza índices para facilitar a busca e recuperação de notas.

### ⎮ Segurança

* __Autenticação do Usuário__: sistema de autenticação simples, com password encriptada com recurso ao bcrypt.

* __Notas​__: encriptação das notas em trânsito e em repouso com recurso ao Fernet.

### ⎮ Recuperação de Falhas

* __Backup Regular__:
Implementação de backups regulares do MongoDB para prevenir perda de dados.

Os backups são feitos sempre que uma modificação é feita na base de dados, nos dados de usuários ou notas. ​Com recurso ao Mongodump.
Dois ficheiros de backup, em formato bson (dados) e json (header), em zip para melhor armazenamento. 

Não foi implementado armazenamento redundante em vários servidores.

### ⎮ Sistema de Arquivos Distribuídos

Utilização do protocolo HTTP para operações síncronas, ou seja, operações CRUD (Create, Read, Update, Delete) e interações diretas do usuário.

### ⎮ Operações em Paralelo

Utilização de threads para atender a várias solicitações simultaneamente com recurso ao threading library. 

### ⎮ Distribuição

As threads fazem distribuição de carga entre as várias portas, permitindo que vários clientes se conectem simultaneamente sem subcarregar uma porta. 




