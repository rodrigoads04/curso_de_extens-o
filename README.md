# 📝 Gerenciador de Tarefas (To-Do List)

Projeto desenvolvido durante o meu curso de extensão para praticar lógica de programação em **Python**. O objetivo foi criar uma aplicação de terminal que permite gerenciar tarefas de forma dinâmica, utilizando conceitos fundamentais da linguagem.

## 🚀 Funcionalidades

O programa funciona como um sistema CRUD básico (Create, Read, Update, Delete):

- **Adicionar Tarefas:** Cria um novo item na lista com status inicial "Pendente".
- **Listar Tarefas:** Exibe todas as tarefas, seus respectivos IDs e o status atual.
- **Concluir Tarefas:** Altera o status de uma tarefa específica para "Concluído".
- **Remover Tarefas:** Exclui uma tarefa da lista utilizando o índice numérico.
- **Saída Segura:** Encerra a execução do loop principal através de uma opção de saída.

## 🛠️ Conceitos Técnicos Aplicados

Neste projeto, apliquei os seguintes conceitos de Python:

- **Estruturas de Dados:** Uso de listas e dicionários para organizar os dados (`{'nome': nome, 'status': False}`).
- **Modularização:** Divisão do código em funções (`def`) para cada ação do sistema.
- **Controle de Fluxo:** Estruturas condicionais (`if/elif/else`) e repetição (`while True`).
- **Manipulação de Índices:** Uso da função `enumerate()` para gerar IDs automáticos para as tarefas.
- **Lógica Booleana:** Controle de status das tarefas (True para concluído, False para pendente).

## 📂 Como executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python seu_arquivo.py
   ```

---
Desenvolvido por [Seu Nome] 👋
