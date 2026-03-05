from services.produtos_service import (
    adicionar_produto,
    listar_produtos,
    remover_produto,
    resumo
)


def iniciar_menu():

    nome_usuario = input("Digite seu nome: ")

    produtos = []
    produtos_removidos = []

    while True:

        print("\n=== MENU ===")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Remover produto")
        print("4 - Ver resumo")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_produto(produtos)

        elif opcao == "2":
            listar_produtos(produtos)

        elif opcao == "3":
            remover_produto(produtos, produtos_removidos)

        elif opcao == "4":
            resumo(nome_usuario, produtos, produtos_removidos)

        elif opcao == "5":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")