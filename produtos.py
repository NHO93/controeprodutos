produtos = []

def adicionar():
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    preco = float(input("Valor do produto: "))
    disponivel = input("Disponível para venda (sim/não): ").lower() == 'sim'
    produto = {
        'nome': nome,
        'descricao': descricao,
        'preco': preco,
        'disponivel': disponivel
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def lista_produtos():
    print("\nLista de produtos: ")
    print("-" *30)
    print("Nome/Preco")
    print("-" *30)
    for produto in sorted(produtos, key=lambda item: item['nome']):
        print(f"{produto['nome']}\tR${produto['preco']: .2f}")

def menu():
    while True:
        print("\nControle de Produtos")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            adicionar()
        elif opcao == '2':
            lista_produtos()
        elif opcao == '3':
            print("Obrigado por usar o nosso sistema! Até a próxima.")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()