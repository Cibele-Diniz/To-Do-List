tarefas = []

def mostrar_tarefas():
    print("\n📋 Lista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("✅ Tarefa adicionada!")
