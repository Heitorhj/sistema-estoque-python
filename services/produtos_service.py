from models.produto import Produto


def adicionar_produto(produtos):
    nome = input("Digite o nome do produto: ")

    produto = Produto(nome)

    produtos.append(produto)

    print(f"Produto '{nome}' adicionado com sucesso.")


def listar_produtos(produtos):

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de produtos:")
        for produto in produtos:
            print(f"- {produto.nome}")


def remover_produto(produtos, produtos_removidos):

    nome = input("Digite o nome do produto a remover: ")

    for produto in produtos:

        if produto.nome == nome:
            produtos.remove(produto)
            produtos_removidos.append(produto)

            print("Produto removido com sucesso.")
            return

    print("Produto não encontrado.")


def resumo(nome, produtos, produtos_removidos):

    print("\n--- RESUMO DA COMPRA ---")
    print(f"Nome: {nome}")
    print(f"Produtos cadastrados: {len(produtos)}")

    if produtos:
        print("\nProdutos atuais:")
        for produto in produtos:
            print(f"- {produto.nome}")
    else:
        print("Nenhum produto cadastrado.")

    if produtos_removidos:
        print("\nProdutos removidos:")
        for produto in produtos_removidos:
            print(f"- {produto.nome}")
    else:
        print("Nenhum produto removido.")