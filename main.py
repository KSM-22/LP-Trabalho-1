# BANCO_DADOS = []

BANCO_DADOS = [
    {'id': 'ABC-123', 'nome': 'Arroz Integral', 'preco': 15.99, 'quantidade': 50, 'categoria': 'Alimentos'},
    {'id': 'DEF-456', 'nome': 'Detergente Multiuso', 'preco': 8.50, 'quantidade': 30, 'categoria': 'Limpeza'},
    {'id': 'GHI-789', 'nome': 'Smartphone X', 'preco': 1299.99, 'quantidade': 10, 'categoria': 'Eletrônicos'},
    {'id': 'JKL-012', 'nome': 'Camiseta Basica', 'preco': 29.90, 'quantidade': 25, 'categoria': 'Vestuário'},
    {'id': 'MNO-345', 'nome': 'Feijao Premium', 'preco': 12.75, 'quantidade': 40, 'categoria': 'Alimentos'}
]
categorias_validas = ("Alimentos", "Limpeza", "Eletrônicos", "Vestuário")


#
#   Espaço reservado para funções auxiliares
#   Essas funções começam com _ que é a convenção utilizada em Python para indicar "uso interno"
#
def _buscar_produto(chave, tipo='id'):
    for produto in BANCO_DADOS:
        if produto[tipo] == chave:
            return produto
    return None


def _verificar_id(id):
    id_parts = id.strip().split('-')
    if len(id_parts) != 2:
        print('Formato de ID inválido. Use o formato "ABC-123".')
        return False
    if not id_parts[0].isalpha():
        print('A primeira parte do ID deve ser somente letras.')
        return False
    if len(id_parts[0]) != 3:
        print('A primeira parte do ID deve ter somente 3 letras.')
        return False
    # Verificar a segunda parte do ID.
    if not id_parts[1].isnumeric():
        print('A segunda parte do ID deve ser somente números.')
        return False
    if len(id_parts[1]) != 3:
        print('A segunda parte do ID ter somente 3 números.')
        return False
    return True


#
#   Espaço reservado para funções principais
#   Essas funções são as que interagem com o usúario e por intermédio de funções internas e manipulação do BANCO_DADOS
#   gerenciam o sistema.
#
def esta_cadastrado(produto_id):
    for produto in BANCO_DADOS:
        if produto['id'] == produto_id:
            return True
    return False


def cadastrar_produto():
    global id
    global nome
    global preco
    global quantidade
    global categoria

    while True:
        id = input('Digite o id do produto (Ex. ABC-123): ')
        if not _verificar_id(id):
            continue
        if esta_cadastrado(id):
            print('Esse ID já está cadastrado, escolha outro.')
        # Se chegar aqui significa que todas as condições estão corretas e pode ir para o proximo laço (while).
        break

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
        BANCO_DADOS.append({'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade, 'categoria': categoria})
        print('Produto cadastrado com sucesso!')
    else:
        print('Produto já existe no banco de dados.')


def buscar_produto():
    print("""=== MENU - BUSCAR PRODUTO ===
    1. Buscar por ID
    2. Buscar por nome
    3. Buscar por categoria""")
    opcao_escolhida_busca = int(input('Digite sua opção:').strip())
    while opcao_escolhida_busca not in range(1, 4):
        print('Opção inválida.')
        opcao_escolhida_busca = int(input('Digite sua opção:').strip())

    global produtos
    if opcao_escolhida_busca == 1:
        id = str(input('Digite o ID do produto: '))
        while not _verificar_id(id):
            id = str(input('Digite o ID do produto: '))
        produto = _buscar_produto(id)
        if not produtos:
            print('Não há nenhum produto com esse ID.')
            return
        produtos = [produto]
    elif opcao_escolhida_busca == 2:
        # TODO: Questionar se produtos podem ter o mesmo nome.
        nome = input('Digite o nome do produto: ').strip()
        produto = _buscar_produto(nome, tipo='nome')
        if not produto:
            print('Não há nenhum produto com esse nome.')
            return
        produtos = [produto]
    elif opcao_escolhida_busca == 3:
        print("""=== Categorias disponiveis ===
    1. Alimentos
    2. Limpeza
    3. Eletrônicos
    4. Vestuário""")
        categoria_escolhida = int(input('Digite a categoria do produto: ').strip())
        while not categoria_escolhida in range(1, 5):
            print('Categoria inválida.')
            categoria_escolhida = int(input('Digite a categoria do produto: ').strip())
        if categoria_escolhida == 1:
            categoria_escolhida = 'Alimentos'
        elif categoria_escolhida == 2:
            categoria_escolhida = 'Limpeza'
        elif categoria_escolhida == 3:
            categoria_escolhida = 'Eletrônicos'
        elif categoria_escolhida == 4:
            categoria_escolhida = 'Vestuário'
        produtos = filter(lambda produto: produto['categoria'] == categoria_escolhida, BANCO_DADOS)
        produtos = list(produtos)
        if len(produtos) == 0:
            print('Não há nenhum produto com essa categoria.')
            return

    for produto in produtos:
        header = f"{'-' * 10} Informações do Produto {'-' * 10}"
        print(f"""{header}
    Identificador Unico(ID): {produto['id']}
    Nome: {produto['nome']}
    Preço: R$ {produto['preco']}
    Quantidade em Estoque: {produto['quantidade']}
    Categoria: {produto['categoria']}
{'-' * len(header)}""")


# Área de execução, é aqui que o Python vai executar o codigo principal para saber qual função chamar.
while True:
    print("""
    === MENU PRINCIPAL ===
    1. Cadastrar produto [FEITO]
    2. Atualizar produto
    3. Remover produto
    4. Listar produtos (ordenar por: nome/preço/estoque)
    5. Buscar produto [FEITO
    6. Relatórios (Valor total/Estoque baixo)
    7. Vender produto
    8. Aplicar desconto
    0. Sair""")
    opcao_escolhida = int(input('Digite sua opção: '))
    if opcao_escolhida == 1:
        cadastrar_produto()
    elif opcao_escolhida == 2:
        pass
    elif opcao_escolhida == 3:
        pass
    elif opcao_escolhida == 4:
        pass
    elif opcao_escolhida == 5:
        buscar_produto()
    elif opcao_escolhida == 6:
        pass
    elif opcao_escolhida == 7:
        pass
    elif opcao_escolhida == 8:
        pass
    elif opcao_escolhida == 0:
        print('Desligando o sistema...')
        break
    else:
        print('Opção inválida.')
