from sistema_crud import SistemaCRUD


def menu():
    """
    Exibe um menu interativo para operações CRUD de pessoas.
    """
    sistema = SistemaCRUD()

    while True:
        print("\nMENU CRUD:")
        print("1 - Criar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Atualizar Pessoa")
        print("4 - Excluir Pessoa")
        print("5 - Exportar para CSV")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("Idade inválida. Use apenas números.")
                continue
            sistema.criar_pessoa(nome, idade)

        elif opcao == "2":
            sistema.listar_pessoas()

        elif opcao == "3":
            try:
                pessoa_id = int(input("ID da pessoa para atualizar: "))
            except ValueError:
                print("ID inválido. Use apenas números.")
                continue

            novo_nome = input("Novo nome: ")
            try:
                nova_idade = int(input("Nova idade: "))
            except ValueError:
                print("Idade inválida. Use apenas números.")
                continue

            confirm = input("Confirma atualização? (s/n): ").lower()
            if confirm == "s":
                sistema.atualizar_pessoa(pessoa_id, novo_nome, nova_idade)
            else:
                print("Atualização cancelada.")

        elif opcao == "4":
            try:
                pessoa_id = int(input("ID da pessoa a excluir: "))
            except ValueError:
                print("ID inválido. Use apenas números.")
                continue

            confirm = input("Confirma exclusão? (s/n): ").lower()
            if confirm == "s":
                sistema.excluir_pessoa(pessoa_id)
            else:
                print("Exclusão cancelada.")

        elif opcao == "5":
            sistema.exportar_csv()

        elif opcao == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
