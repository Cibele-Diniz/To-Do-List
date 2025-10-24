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
    
def remover_tarefa():
    mostrar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para remover: "))
        tarefas.pop(indice - 1)
        print("❌ Tarefa removida!")
    except (ValueError, IndexError):
        print("Número inválido!")
