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

* __Camada de Lógica de Negócios__: Contém a lógica principal do sistema. É responsável pela autenticação do usuário, criptografia de notas e distribuição eficiente. 
Recebe comandos da camada de apresentação e processa operações correspondentes. Utiliza o RabbitMQ para comunicação assíncrona com a camada de armazenamento distribuído (MongoDB) e HTTP para operações síncronas, ou seja, operações CRUD (Create, Read, Update, Delete) e interações diretas do usuário.

* __Camada de Dados__: Utiliza o MongoDB como banco de dados para armazenar notas de texto. Implementa mecanismos de persistência eficiente e recuperação de falhas usando as capacidades do MongoDB.

### ⎮ Mecanismo de Nomeação e Localização
Adotamos um sistema de UUIDs (Identificadores Únicos Universais) para cada nota em que usamos o MongoDB para armazenar os documentos de notas, associando cada nota ao identificador, facilitando a localização e referência.

A camada de lógica de negócios utiliza índices eficientes para facilitar a busca e recuperação de notas.

### ⎮ Segurança

* __Autenticação do Usuário__: para a autenticação utilizamos tokens JWT.

* __Criptografia__:
Criptografamos as notas em trânsito e em reposo usando HTTPS para comunicação segura.

### ⎮ Recuperação de Falhas

* __Backup Regular__:
Implementação de backups regulares do MongoDB para prevenir perda de dados.
Armazenamento redundante em vários servidores para maior resiliência.

* __Recuperação de Falhas__:
Para a recuperação de falhas aproveitamos as capacidades de replicação e recuperação do MongoDB para lidar com mensagens perdidas ou não entregues.

### ⎮ Sistema de Arquivos Distribuídos

Utilizamos o protocolo HTTP para operações síncronas, ou seja, operações CRUD (Create, Read, Update, Delete) e interações diretas do usuário.

E utilizamos o protocolo AMQP para tarefas que podem ser executadas de forma assíncrona, como replicação de notas entre servidores, backup regular, e outras operações de fundo.

### ⌊ Operações em Paralelo

Utilizamos threads ou processos paralelos para atender a várias solicitações simultaneamente.




