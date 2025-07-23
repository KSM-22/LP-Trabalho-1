from datetime import datetime

# BANCO_DADOS = []
# TODO: match case no id
HISTORICO_VENDAS = []
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
        id = input('Digite o id do produto (Ex. ABC-123): ').upper()
        if not _verificar_id(id):
            continue
        if esta_cadastrado(id):
            print('Esse ID já está cadastrado, escolha outro.')
            continue
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


def atualizar_produto():
    print('—' * 20 + f'{'ATUALIZAR PRODUTO':^21}' + '—' * 19)
    id_local = input('Digite o ID do produto: ').upper()
    if not _verificar_id(id_local):
        return

    produto = _buscar_produto(id_local)
    if not produto:
        print('Produto não encontrado.')
        return

    print(f"""
Identificador Unico(ID): {produto['id']}
Nome: {produto['nome']}
Preço: R$ {produto['preco']}
Quantidade em Estoque: {produto['quantidade']}
Categoria: {produto['categoria']}""")
    print("""
    1. Atualizar preço
    2. Atualizar nome
    3. Atualizar quantidade
    """)

    try:
        opcao = int(input('Digite sua opção: ').strip())
        if opcao == 1:
            try:
                novo_preco = float(input('Digite o novo preço: R$ '))
                if novo_preco > 0:
                    produto['preco'] = novo_preco
                    print('Preço atualizado com sucesso!')
                else:
                    print('Preço inválido. Digite um valor positivo.')
            except ValueError:
                print('Digite um valor numérico válido.')

        elif opcao == 2:
            novo_nome = input('Digite o novo nome: ').strip()
            if novo_nome.replace(' ', '').isalnum():
                produto['nome'] = novo_nome
                print('Nome atualizado com sucesso!')
            else:
                print('Nome inválido, use apenas letras, números e espaços.')

        elif opcao == 3:
            try:
                ajuste = input('Digite a quantidade (use + ou - para ajustar) Ex. +10: ')
                if ajuste.startswith('+'):
                    quantidade = int(ajuste[1:])
                    produto['quantidade'] += quantidade
                    print(f'Adicionadas {quantidade} unidades ao estoque.')
                elif ajuste.startswith('-'):
                    quantidade = int(ajuste[1:])
                    if produto['quantidade'] >= quantidade:
                        produto['quantidade'] -= quantidade
                        print(f'Removidas {quantidade} unidades do estoque.')
                        if produto['quantidade'] == 0:
                            print('ALERTA: Estoque esgotado!')
                    else:
                        print('Quantidade insuficiente em estoque.')
                else:
                    print('Use + ou - para ajustar a quantidade.')
            except ValueError:
                print('Digite um número válido.')
        else:
            print('Opção inválida.')
    except ValueError:
        print('Digite uma opção válida.')




def remover_produto():
    print('—' * 20 + f'{'REMOVER PRODUTO':^21}' + '—' * 19)
    id = input('Digite o ID do produto: ').upper()
    if not _verificar_id(id):
        return

    produto = _buscar_produto(id)
    if not produto:
        print('Produto não encontrado.')
        return

    if produto['quantidade'] == 0:
        print('Não é possível remover um produto sem estoque.')
        return

    print(f"\nVocê realmente deseja remover {produto['nome']}? (S/N)")
    confirmacao = input().upper()

    if confirmacao == 'S':
        BANCO_DADOS.remove(produto)
        print('Produto removido com sucesso!')
    else:
        print('Operação cancelada.')

def listar_produto():
    estoque_baixo = 15
    print('—' * 20 + f'{'LISTAR PRODUTOS':^21}' + '—' * 19 +
    """
    1. Listar todos os produtos
    2. Filtrar por nome
    3. Filtrar por ID 
    4. Filtrar por categoria
    5. Mostrar produtos com estoque baixo
    6. Ordenar produtos por nome
    7. Ordenar produtos por preço
    8. Ordenar produtos por estoque
    """)

    try:
        opcao = int(input('Digite sua opção: ').strip())
        produtos = BANCO_DADOS.copy()

        if opcao == 1:
            pass  # Lista todos
        elif opcao == 2:
            nome = input('Digite o nome para filtrar: ').strip()
            produtos = [p for p in produtos if nome.lower() in p['nome'].lower()]
        elif opcao == 3:
            id = input('Digite o ID para filtrar: ').upper()
            produtos = [p for p in produtos if id in p['id']]
        elif opcao == 4:
            print('\nCategorias disponíveis:')
            for i, cat in enumerate(categorias_validas, 1):
                print(f'{i}. {cat}')
            cat_num = int(input('\nEscolha o número da categoria: '))
            if 1 <= cat_num <= len(categorias_validas):
                cat = categorias_validas[cat_num - 1]
                produtos = [p for p in produtos if p['categoria'] == cat]
        elif opcao == 5:
            produtos = [p for p in produtos if p['quantidade'] < estoque_baixo]
        elif opcao in [6, 7, 8]:
            try:
                print('—' * 21 + f'{'ORDENAR POR:':^18}' + '—' * 21 +
    '''
    1. Crescente
    2. Decrescente
    '''
                     )
                ordem = int(input("Digite sua opção: ").strip())

                if ordem not in [1, 2]:
                    print("Opção de ordenação inválida!")
                    return

                reverse = ordem == 2
                if opcao == 6:
                    produtos.sort(key=lambda x: x['nome'], reverse=reverse)
                elif opcao == 7:
                    produtos.sort(key=lambda x: x['preco'], reverse=reverse)
                else:  # opcao == 8
                    produtos.sort(key=lambda x: x['quantidade'], reverse=reverse)
            except ValueError:
                print("Digite uma opção válida!")
                return
        else:
            print('Opção inválida!')
            return

        if not produtos:
            print('Nenhum produto encontrado!')
            return

        for produto in produtos:
            header = ('—' * 16 + f'{'INFORMAÇÕES DO PRODUTO':^28}' + '—' * 16)
            print(f"""
    {header}
    Identificador Unico(ID): {produto['id']}
    Nome: {produto['nome']}
    Preço: R$ {produto['preco']}
    Quantidade em Estoque: {produto['quantidade']}
    Categoria: {produto['categoria']}\n""")

    except ValueError:
        print('Digite uma opção válida!')

def buscar_produto():
    print('—' * 20 + f'{'BUSCAR PRODUTO':^20}' + '—' * 20 +
    """
    1. Buscar por ID
    2. Buscar por nome
    3. Buscar por categoria
    """)
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
        if not produto:
            print('Não há nenhum produto com esse ID.')
            return
        produtos = [produto]
    elif opcao_escolhida_busca == 2:
        nome = input('Digite o nome do produto: ').strip()
        produto = _buscar_produto(nome, tipo='nome')
        if not produto:
            print('Não há nenhum produto com esse nome.')
            return
        produtos = [produto]
    elif opcao_escolhida_busca == 3:
        print('—' * 16 + f'{'CATEGORIAS DISPONÍVEIS':^28}' + '—' * 16 +
    """
    1. Alimentos
    2. Limpeza
    3. Eletrônicos
    4. Vestuário\n""")
        categoria_escolhida = int(input('Digite a categoria do produto: ').strip())
        print('')
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
        header = ('—' * 16 + f'{'INFORMAÇÕES DO PRODUTO':^28}' + '—' * 16)
        print(f"""{header}
    Identificador Unico(ID): {produto['id']}
    Nome: {produto['nome']}
    Preço: R$ {produto['preco']}
    Quantidade em Estoque: {produto['quantidade']}
    Categoria: {produto['categoria']}\n""")

def vender_produto():
    print('—' * 20 + f'{'VENDER PRODUTO':^20}' + '—' * 20)

    vendas_atuais = []
    valor_total_vendas = 0
    data_venda = datetime.now()

    while True:
        id = input('Digite o ID do produto: ').upper()
        if not _verificar_id(id):
            continue

        produto = _buscar_produto(id)
        if not produto:
            print('Produto não encontrado.')
            continue

        try:
            quantidade = int(input('Digite a quantidade desejada: '))
            if quantidade <= 0:
                print('Quantidade inválida, digite um valor positivo.')
                continue
        except ValueError:
            print('Digite um número válido.')
            continue

        if quantidade > produto['quantidade']:
            print(f"Estoque insuficiente. Disponível: {produto['quantidade']}")
            continue

        total = produto['preco'] * quantidade

        print(f"\nConfirmar venda de {quantidade} unidade(s) de {produto['nome']}?")
        print(f"Valor total: R$ {total:.2f}")
        confirmacao = input("Digite S para confirmar: ").upper()

        if confirmacao != 'S':
            print('Venda cancelada.')
            continue

        produto['quantidade'] -= quantidade
        valor_total_vendas += total

        venda = {
            'data': data_venda,
            'produto': produto['nome'],
            'quantidade': quantidade,
            'valor_unitario': produto['preco'],
            'valor_total': total
        }

        HISTORICO_VENDAS.append(venda)
        vendas_atuais.append(venda)

        continuar = input("\nDeseja vender mais produtos? (S/N): ").upper()
        if continuar != 'S':
            break

    if vendas_atuais:
        print('\n' + '—' * 24 + f'{'RECIBO':^12}' + '—' * 24)
        print(f"Data: {data_venda.strftime('%d/%m/%Y %H:%M:%S')}")
        print('—' * 60)
        print(f"{'Produto':<25} {'Qtd':>5} {'Valor Unit.':>12} {'Total':>12}")
        print('—' * 60)

        for venda in vendas_atuais:
            print(
                f"{venda['produto']:<25} {venda['quantidade']:>5} {venda['valor_unitario']:>12.2f} {venda['valor_total']:>12.2f}")

        print('—' * 60)
        print(f"Total de itens vendidos: {len(vendas_atuais)}")
        print(f"Valor total da venda: R$ {valor_total_vendas:.2f}")


def gerar_relatorios():
    print('—' * 20 + f'{'RELATÓRIOS':^20}' + '—' * 20)

    # Calcula e exibe valor total em estoque
    valor_total = sum(p['preco'] * p['quantidade'] for p in BANCO_DADOS)
    print(f'\nValor total em estoque: R$ {valor_total:.2f}')

    # Verifica e exibe produtos com estoque baixo
    estoque_baixo = 15
    produtos_baixo = [p for p in BANCO_DADOS if p['quantidade'] < estoque_baixo]

    print(f'\nProdutos com estoque baixo(Abaixo de {estoque_baixo} unidades):')
    if not produtos_baixo:
        print('Não há produtos com estoque baixo.')
    else:
        for produto in produtos_baixo:
            print(f"""
    Nome: {produto['nome']}
    Quantidade atual: {produto['quantidade']}
    Categoria: {produto['categoria']}""")


def aplicar_desconto():
    print('—' * 20 + f'{'APLICAR DESCONTO':^20}' + '—' * 20)
    print('\nCategorias disponíveis:')
    for i, cat in enumerate(categorias_validas, 1):
        print(f'{i}. {cat}')

    try:
        cat_num = int(input('\nEscolha o número da categoria: '))
        if not 1 <= cat_num <= len(categorias_validas):
            print('Categoria inválida!')
            return

        percentual = float(input('Digite o percentual de desconto (1-100): '))
        if not 0 < percentual <= 100:
            print('Percentual inválido!')
            return

        categoria = categorias_validas[cat_num - 1]
        produtos_categoria = [p for p in BANCO_DADOS if p['categoria'] == categoria]

        if not produtos_categoria:
            print(f'Nenhum produto encontrado na categoria {categoria}')
            return

        for produto in produtos_categoria:
            desconto = produto['preco'] * (percentual / 100)
            preco_com_desconto = produto['preco'] - desconto

            print(f"\n{produto['nome']}:")
            print(f"Preço original: R$ {produto['preco']:.2f}")
            print(f"Com desconto ({percentual}%): R$ {preco_com_desconto:.2f}")

            confirmacao = input('\nAplicar desconto? (S/N): ').upper()
            if confirmacao == 'S':
                produto['preco'] = preco_com_desconto
                print('Desconto aplicado com sucesso!')
            else:
                print('Desconto não aplicado.')

    except ValueError:
        print('Digite valores numéricos válidos!')


# Área de execução, é aqui que o Python vai executar o codigo principal para saber qual função chamar.

while True:
    print('—' * 20 + f'{'MENU PRINCIPAL':^20}' + '—' * 20 +
    '''
    1. Cadastrar produto
    2. Atualizar produto
    3. Remover produto
    4. Listar produtos
    5. Buscar produto
    6. Relatórios (Valor total/Estoque baixo)
    7. Vender produto
    8. Aplicar desconto
    0. Sair
    ''')
    opcao_escolhida = int(input('Digite sua opção: '))
    if opcao_escolhida == 1:
        cadastrar_produto()
    elif opcao_escolhida == 2:
        atualizar_produto()
    elif opcao_escolhida == 3:
        remover_produto()
    elif opcao_escolhida == 4:
        listar_produto()
    elif opcao_escolhida == 5:
        buscar_produto()
    elif opcao_escolhida == 6:
        gerar_relatorios()
    elif opcao_escolhida == 7:
        vender_produto()
    elif opcao_escolhida == 8:
        aplicar_desconto()
    elif opcao_escolhida == 0:
        print('Desligando o sistema...')
        break
    else:
        print('Opção inválida.')
