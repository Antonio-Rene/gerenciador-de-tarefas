def menu():
    print("\n1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Editar tarefa")
    print("4. Remover tarefa")
    print("5. Concluir tarefa")
    print("6. Sair")

def executar():
    gerenciador = GerenciadorDeTarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            data_vencimento = input("Data de vencimento (AAAA-MM-DD): ")
            gerenciador.adicionar_tarefa(titulo, descricao, data_vencimento)

        elif opcao == '2':
            gerenciador.listar_tarefas()

        elif opcao == '3':
            indice = int(input("Índice da tarefa a editar: "))
            novo_titulo = input("Novo título: ")
            nova_descricao = input("Nova descrição: ")
            nova_data_vencimento = input("Nova data de vencimento: ")
            gerenciador.editar_tarefa(indice, novo_titulo, nova_descricao, nova_data_vencimento)

        elif opcao == '4':
            indice = int(input("Índice da tarefa a remover: "))
            gerenciador.remover_tarefa(indice)

        elif opcao == '5':
            indice = int(input("Índice da tarefa a concluir: "))
            gerenciador.concluir_tarefa(indice)

        elif opcao == '6':
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    executar()
