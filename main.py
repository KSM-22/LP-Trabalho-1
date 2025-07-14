BANCO_DADOS = []


def esta_cadastrado(produto):
    for produto_banco in BANCO_DADOS:
        if produto_banco['nome'] == produto:
            return True
    return False


def adiconar_produto():
    global nome
    global preco
    global quantidade
    global categoria

    while True:
        nome = input('Digite o nome do produto: ').strip()
        # if all(c.isalnum() or c.isspace() for c in nome) and nome:
        if nome.replace(' ', '').isalnum():
            break
        print('Nome inválido, use apenas letras, números e espaços.')

    while True:
        try:
            preco = float(input('Digite o preço do produto: R$ '))
            if preco > 0:
                break
            print('Preço inválido, digite um valor positivo.')
        except ValueError:
            print('Digite um valor numérico válido.')

    while True:
        try:
            quantidade = int(input('Digite a quantidade do produto: '))
            if quantidade > 0:
                break
            print('Quantidade inválida, digite um valor positivo maior que zero.')
        except ValueError:
            print('Digite um número inteiro válido.')

    categorias_validas = ("Alimentos", "Limpeza", "Eletrônicos", "Vestuário")
    while True:
        print('\nCategorias disponíveis:')
        for i, cat in enumerate(categorias_validas, 1):
            print(f'{i}. {cat}')
        try:
            opcao = int(input('\nEscolha o número da categoria: '))

            if 1 <= opcao <= len(categorias_validas):
                categoria = categorias_validas[opcao - 1]
                break
            print('Escolha uma opção válida.')
        except ValueError:
            print('Digite um número válido.')

    if not esta_cadastrado(nome):
        BANCO_DADOS.append({'nome': nome, 'preco': preco, 'quantidade': quantidade, 'categoria': categoria})
        print('Produto cadastrado com sucesso!')
    else:
        print('Produto já existe no banco de dados.')


adiconar_produto()
print(BANCO_DADOS)
