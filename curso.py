tarefas = []

def adicionar():
    nome = input("Nome da tarefa: ")
    tarefas.append({"nome": nome, "status": False})
    print("Tarefa adicionada com sucesso!")

def listar():
    if not tarefas:
        print("A lista está vazia.")
        return
    for c, v in enumerate(tarefas):
        # O status é definido com base no valor booleano
        status = 'Concluido' if v['status'] else 'Pendente'
        print(f'id: {c} - {v["nome"]}: [{status}]')

def concluir():
    listar()
    if tarefas:
        indice = int(input("Número da tarefa para concluir: "))
        if 0 <= indice < len(tarefas):
            tarefas[indice]['status'] = True
            print("Tarefa concluída!")
        else:
            print("ID inválido.")

def remover():
    listar()
    if tarefas:
        indice = int(input("Número da tarefa para remover: "))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida!")
        else:
            print("ID inválido.")

while True:
    print("\n1 - Adicionar \n2 - Lista de Tarefas \n3 - Concluir tarefa \n4 - Remover Tarefa \n0 - Sair")
    op = input("Digite sua Opção: ")

    if op == "1":
        adicionar()
    elif op == "2":
        listar()
    elif op == "3":
        concluir()
    elif op == "4":
        remover()
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opção Inválida")
