tarefas = []

def mostrar_tarefas():
    print("Lista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def remover_tarefa():
    mostrar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para remover: "))
        tarefas.pop(indice - 1)
        print("Tarefa removida!")
    except (ValueError, IndexError):
        print("Número inválido!")

while True:
<<<<<<< HEAD
    print("To-Do List")
=======
    print("To-Do List em Python")
>>>>>>> ee09924ce502b46b2203f1f77330615d6b017072
    print("1 - Mostrar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("0 - Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        mostrar_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")