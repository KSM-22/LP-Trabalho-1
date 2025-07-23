# Lista para armazenar o histórico de todas as vendas realizadas
HISTORICO_VENDAS = []

# Banco de dados inicial com produtos pré-cadastrados para teste do sistema
BANCO_DADOS = [
    {'id': 'ABC-123', 'nome': 'Arroz Integral', 'preco': 15.99, 'quantidade': 50, 'categoria': 'Alimentos'},
    {'id': 'DEF-456', 'nome': 'Detergente Multiuso', 'preco': 8.50, 'quantidade': 30, 'categoria': 'Limpeza'},
    {'id': 'GHI-789', 'nome': 'Smartphone X', 'preco': 1299.99, 'quantidade': 10, 'categoria': 'Eletrônicos'},
    {'id': 'JKL-012', 'nome': 'Camiseta Basica', 'preco': 29.90, 'quantidade': 25, 'categoria': 'Vestuário'},
    {'id': 'MNO-345', 'nome': 'Feijao Premium', 'preco': 12.75, 'quantidade': 40, 'categoria': 'Alimentos'}
]
# Tupla com as categorias válidas para classificação dos produtos
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
# Função que verifica se um produto com o ID fornecido já existe no banco de dados
def esta_cadastrado(produto_id):
    # Percorre todos os produtos no banco de dados
    for produto in BANCO_DADOS:
        # Se encontrar um produto com o ID fornecido, retorna True
        if produto['id'] == produto_id:
            return True
    # Se não encontrar nenhum produto com o ID fornecido, retorna False
    return False


# Função para cadastrar um novo produto no sistema
# Solicita ao usuário todas as informações necessárias e realiza validações para garantir dados corretos
def cadastrar_produto():
    # Declaração de variáveis globais para armazenar os dados do produto
    global id
    global nome
    global preco
    global quantidade
    global categoria

    # Loop para validação do ID do produto
    while True:
        id = input('Digite o id do produto (Ex. ABC-123): ').upper()
        # Verifica se o ID está no formato correto
        if not _verificar_id(id):
            continue
        # Verifica se o ID já está cadastrado
        if esta_cadastrado(id):
            print('Esse ID já está cadastrado, escolha outro.')
            continue
        # Se chegar aqui significa que todas as condições estão corretas e pode ir para o proximo laço (while).
        break

    # Loop para validação do nome do produto
    while True:
        nome = input('Digite o nome do produto: ').strip()
        # Verifica se o nome contém apenas caracteres alfanuméricos e espaços
        # if all(c.isalnum() or c.isspace() for c in nome) and nome:
        if nome.replace(' ', '').isalnum():
            break
        print('Nome inválido, use apenas letras, números e espaços.')

    # Loop para validação do preço do produto
    while True:
        try:
            preco = float(input('Digite o preço do produto: R$ '))
            # Verifica se o preço é um valor positivo
            if preco > 0:
                break
            print('Preço inválido, digite um valor positivo.')
        except ValueError:
            print('Digite um valor numérico válido.')

    # Loop para validação da quantidade do produto
    while True:
        try:
            quantidade = int(input('Digite a quantidade do produto: '))
            # Verifica se a quantidade é um valor positivo maior que zero
            if quantidade > 0:
                break
            print('Quantidade inválida, digite um valor positivo maior que zero.')
        except ValueError:
            print('Digite um número inteiro válido.')

    # Loop para seleção da categoria do produto
    while True:
        print('\nCategorias disponíveis:')
        # Exibe as categorias disponíveis com numeração
        for i, cat in enumerate(categorias_validas, 1):
            print(f'{i}. {cat}')
        try:
            opcao = int(input('\nEscolha o número da categoria: '))

            # Verifica se a opção escolhida é válida
            if 1 <= opcao <= len(categorias_validas):
                categoria = categorias_validas[opcao - 1]
                break
            print('Escolha uma opção válida.')
        except ValueError:
            print('Digite um número válido.')

    # Verifica se já existe um produto com o mesmo nome
    if not esta_cadastrado(nome):
        # Adiciona o novo produto ao banco de dados
        BANCO_DADOS.append({'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade, 'categoria': categoria})
        print('Produto cadastrado com sucesso!')
    else:
        print('Produto já existe no banco de dados.')


# Função para atualizar informações de um produto existente no sistema
def atualizar_produto():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'ATUALIZAR PRODUTO':^21}' + '—' * 19)
    # Solicita o ID do produto a ser atualizado
    id_local = input('Digite o ID do produto: ').upper()
    # Verifica se o ID está no formato correto
    if not _verificar_id(id_local):
        return

    # Busca o produto pelo ID informado
    produto = _buscar_produto(id_local)
    # Se o produto não for encontrado, exibe mensagem e encerra a função
    if not produto:
        print('Produto não encontrado.')
        return

    # Exibe as informações atuais do produto
    print(f"""
Identificador Unico(ID): {produto['id']}
Nome: {produto['nome']}
Preço: R$ {produto['preco']}
Quantidade em Estoque: {produto['quantidade']}
Categoria: {produto['categoria']}""")
    # Exibe o menu de opções para atualização
    print("""
    1. Atualizar preço
    2. Atualizar nome
    3. Atualizar quantidade
    """)

    try:
        # Solicita a opção desejada
        opcao = int(input('Digite sua opção: ').strip())
        if opcao == 1:
            # Opção para atualizar o preço
            try:
                novo_preco = float(input('Digite o novo preço: R$ '))
                # Verifica se o novo preço é válido
                if novo_preco > 0:
                    produto['preco'] = novo_preco
                    print('Preço atualizado com sucesso!')
                else:
                    print('Preço inválido. Digite um valor positivo.')
            except ValueError:
                print('Digite um valor numérico válido.')

        elif opcao == 2:
            # Opção para atualizar o nome
            novo_nome = input('Digite o novo nome: ').strip()
            # Verifica se o novo nome é válido
            if novo_nome.replace(' ', '').isalnum():
                produto['nome'] = novo_nome
                print('Nome atualizado com sucesso!')
            else:
                print('Nome inválido, use apenas letras, números e espaços.')

        elif opcao == 3:
            # Opção para atualizar a quantidade em estoque
            try:
                ajuste = input('Digite a quantidade (use + ou - para ajustar) Ex. +10: ')
                # Para adicionar ao estoque
                if ajuste.startswith('+'):
                    quantidade = int(ajuste[1:])
                    produto['quantidade'] += quantidade
                    print(f'Adicionadas {quantidade} unidades ao estoque.')
                # Para remover do estoque
                elif ajuste.startswith('-'):
                    quantidade = int(ajuste[1:])
                    # Verifica se há quantidade suficiente em estoque
                    if produto['quantidade'] >= quantidade:
                        produto['quantidade'] -= quantidade
                        print(f'Removidas {quantidade} unidades do estoque.')
                        # Alerta se o estoque ficar zerado
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


# Função para remover um produto do sistema
def remover_produto():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'REMOVER PRODUTO':^21}' + '—' * 19)
    # Solicita o ID do produto a ser removido
    id = input('Digite o ID do produto: ').upper()
    # Verifica se o ID está no formato correto
    if not _verificar_id(id):
        return

    # Busca o produto pelo ID informado
    produto = _buscar_produto(id)
    # Se o produto não for encontrado, exibe mensagem e encerra a função
    if not produto:
        print('Produto não encontrado.')
        return

    # Verifica se o produto tem estoque zero
    if produto['quantidade'] == 0:
        print('Não é possível remover um produto sem estoque.')
        return

    # Solicita confirmação do usuário para remover o produto
    print(f"\nVocê realmente deseja remover {produto['nome']}? (S/N)")
    confirmacao = input().upper()

    # Remove o produto se o usuário confirmar
    if confirmacao == 'S':
        BANCO_DADOS.remove(produto)
        print('Produto removido com sucesso!')
    else:
        print('Operação cancelada.')


# Função para listar produtos com diversas opções de filtragem e ordenação
def listar_produto():
    # Define o limite para considerar um estoque como baixo
    estoque_baixo = 15
    # Exibe o cabeçalho da função e o menu de opções
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
        # Solicita a opção desejada
        opcao = int(input('Digite sua opção: ').strip())
        # Cria uma cópia do banco de dados para não modificar o original
        produtos = BANCO_DADOS.copy()

        if opcao == 1:
            pass  # Lista todos os produtos sem filtro
        elif opcao == 2:
            # Filtra produtos por nome (busca parcial, case-insensitive)
            nome = input('Digite o nome para filtrar: ').strip()
            produtos = [p for p in produtos if nome.lower() in p['nome'].lower()]
        elif opcao == 3:
            # Filtra produtos por ID (busca parcial)
            id = input('Digite o ID para filtrar: ').upper()
            produtos = [p for p in produtos if id in p['id']]
        elif opcao == 4:
            # Filtra produtos por categoria
            print('\nCategorias disponíveis:')
            for i, cat in enumerate(categorias_validas, 1):
                print(f'{i}. {cat}')
            cat_num = int(input('\nEscolha o número da categoria: '))
            # Verifica se a categoria escolhida é válida
            if 1 <= cat_num <= len(categorias_validas):
                cat = categorias_validas[cat_num - 1]
                produtos = [p for p in produtos if p['categoria'] == cat]
        elif opcao == 5:
            # Filtra produtos com estoque baixo
            produtos = [p for p in produtos if p['quantidade'] < estoque_baixo]
        elif opcao in [6, 7, 8]:
            # Opções de ordenação
            try:
                print('—' * 21 + f'{'ORDENAR POR:':^18}' + '—' * 21 +
    '''
    1. Crescente
    2. Decrescente
    '''
                     )
                ordem = int(input("Digite sua opção: ").strip())

                # Verifica se a opção de ordenação é válida
                if ordem not in [1, 2]:
                    print("Opção de ordenação inválida!")
                    return

                # Define se a ordenação será crescente ou decrescente
                reverse = ordem == 2
                if opcao == 6:
                    # Ordena por nome
                    produtos.sort(key=lambda x: x['nome'], reverse=reverse)
                elif opcao == 7:
                    # Ordena por preço
                    produtos.sort(key=lambda x: x['preco'], reverse=reverse)
                else:  # opcao == 8
                    # Ordena por quantidade em estoque
                    produtos.sort(key=lambda x: x['quantidade'], reverse=reverse)
            except ValueError:
                print("Digite uma opção válida!")
                return
        else:
            print('Opção inválida!')
            return

        # Verifica se foram encontrados produtos após a filtragem
        if not produtos:
            print('Nenhum produto encontrado!')
            return

        # Exibe as informações de cada produto encontrado
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


# Função para buscar produtos específicos no sistema por diferentes critérios
def buscar_produto():
    # Exibe o cabeçalho da função e o menu de opções de busca
    print('—' * 20 + f'{'BUSCAR PRODUTO':^20}' + '—' * 20 +
    """
    1. Buscar por ID
    2. Buscar por nome
    3. Buscar por categoria
    """)
    # Solicita a opção de busca desejada
    opcao_escolhida_busca = int(input('Digite sua opção:').strip())
    # Valida a opção escolhida
    while opcao_escolhida_busca not in range(1, 4):
        print('Opção inválida.')
        opcao_escolhida_busca = int(input('Digite sua opção:').strip())

    # Declara a variável global para armazenar os produtos encontrados
    global produtos
    if opcao_escolhida_busca == 1:
        # Opção 1: Busca por ID
        id = str(input('Digite o ID do produto: '))
        # Valida o formato do ID
        while not _verificar_id(id):
            id = str(input('Digite o ID do produto: '))
        # Busca o produto pelo ID
        produto = _buscar_produto(id)
        if not produto:
            print('Não há nenhum produto com esse ID.')
            return
        # Armazena o produto encontrado em uma lista
        produtos = [produto]
    elif opcao_escolhida_busca == 2:
        # Opção 2: Busca por nome
        nome = input('Digite o nome do produto: ').strip()
        # Busca o produto pelo nome exato
        produto = _buscar_produto(nome, tipo='nome')
        if not produto:
            print('Não há nenhum produto com esse nome.')
            return
        # Armazena o produto encontrado em uma lista
        produtos = [produto]
    elif opcao_escolhida_busca == 3:
        # Opção 3: Busca por categoria
        # Exibe as categorias disponíveis
        print('—' * 16 + f'{'CATEGORIAS DISPONÍVEIS':^28}' + '—' * 16 +
    """
    1. Alimentos
    2. Limpeza
    3. Eletrônicos
    4. Vestuário\n""")
        # Solicita a categoria desejada
        categoria_escolhida = int(input('Digite a categoria do produto: ').strip())
        print('')
        # Valida a categoria escolhida
        while not categoria_escolhida in range(1, 5):
            print('Categoria inválida.')
            categoria_escolhida = int(input('Digite a categoria do produto: ').strip())
        # Converte o número da categoria para o nome correspondente
        if categoria_escolhida == 1:
            categoria_escolhida = 'Alimentos'
        elif categoria_escolhida == 2:
            categoria_escolhida = 'Limpeza'
        elif categoria_escolhida == 3:
            categoria_escolhida = 'Eletrônicos'
        elif categoria_escolhida == 4:
            categoria_escolhida = 'Vestuário'
        # Filtra os produtos pela categoria escolhida
        produtos = filter(lambda produto: produto['categoria'] == categoria_escolhida, BANCO_DADOS)
        produtos = list(produtos)
        # Verifica se foram encontrados produtos na categoria
        if len(produtos) == 0:
            print('Não há nenhum produto com essa categoria.')
            return

    # Exibe as informações de cada produto encontrado
    for produto in produtos:
        # Cria um cabeçalho formatado para a exibição
        header = ('—' * 16 + f'{'INFORMAÇÕES DO PRODUTO':^28}' + '—' * 16)
        # Exibe todas as informações do produto
        print(f"""{header}
    Identificador Unico(ID): {produto['id']}
    Nome: {produto['nome']}
    Preço: R$ {produto['preco']}
    Quantidade em Estoque: {produto['quantidade']}
    Categoria: {produto['categoria']}\n""")


# Função para registrar a venda de produtos e gerar um recibo
def vender_produto():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'VENDER PRODUTO':^20}' + '—' * 20)

    # Inicializa variáveis para armazenar as vendas da sessão atual
    vendas_atuais = []
    valor_total_vendas = 0
    # Solicita a data da venda no formato dia/mês/ano
    data_venda = f'{input('Digite o dia: ')}/{input('Digite o mês: ')}/{input("Digite o ano: ")}'

    # Loop para adicionar produtos à venda
    while True:
        # Solicita o ID do produto a ser vendido
        id = input('Digite o ID do produto: ').upper()
        # Verifica se o ID está no formato correto
        if not _verificar_id(id):
            continue

        # Busca o produto pelo ID informado
        produto = _buscar_produto(id)
        # Se o produto não for encontrado, exibe mensagem e continua o loop
        if not produto:
            print('Produto não encontrado.')
            continue

        try:
            # Solicita a quantidade desejada
            quantidade = int(input('Digite a quantidade desejada: '))
            # Verifica se a quantidade é válida (maior que zero)
            if quantidade <= 0:
                print('Quantidade inválida, digite um valor positivo.')
                continue
        except ValueError:
            print('Digite um número válido.')
            continue

        # Verifica se há estoque suficiente
        if quantidade > produto['quantidade']:
            print(f"Estoque insuficiente. Disponível: {produto['quantidade']}")
            continue

        # Calcula o valor total da venda deste produto
        total = produto['preco'] * quantidade

        # Solicita confirmação da venda
        print(f"\nConfirmar venda de {quantidade} unidade(s) de {produto['nome']}?")
        print(f"Valor total: R$ {total:.2f}")
        confirmacao = input("Digite S para confirmar: ").upper()

        # Se não confirmado, cancela esta venda e continua o loop
        if confirmacao != 'S':
            print('Venda cancelada.')
            continue

        # Atualiza o estoque do produto
        produto['quantidade'] -= quantidade
        # Adiciona o valor ao total de vendas
        valor_total_vendas += total

        # Cria um registro da venda
        venda = {
            'data': data_venda,
            'produto': produto['nome'],
            'quantidade': quantidade,
            'valor_unitario': produto['preco'],
            'valor_total': total
        }

        # Adiciona a venda ao histórico geral e à lista de vendas atuais
        HISTORICO_VENDAS.append(venda)
        vendas_atuais.append(venda)

        # Pergunta se deseja continuar vendendo
        continuar = input("\nDeseja vender mais produtos? (S/N): ").upper()
        if continuar != 'S':
            break

    # Verifica se houve vendas para gerar o recibo
    if vendas_atuais:
        # Exibe o cabeçalho do recibo
        print('\n' + '—' * 24 + f'{'RECIBO':^12}' + '—' * 24)
        print(f"Data: {data_venda}")
        print('—' * 60)
        # Exibe o cabeçalho das colunas do recibo
        print(f"{'Produto':<25} {'Qtd':>5} {'Valor Unit.':>12} {'Total':>12}")
        print('—' * 60)

        # Exibe os detalhes de cada produto vendido
        for venda in vendas_atuais:
            print(
                f"{venda['produto']:<25} {venda['quantidade']:>5} {venda['valor_unitario']:>12.2f} {venda['valor_total']:>12.2f}")

        # Exibe o rodapé do recibo com os totais
        print('—' * 60)
        print(f"Total de itens vendidos: {len(vendas_atuais)}")
        print(f"Valor total da venda: R$ {valor_total_vendas:.2f}")


# Função para gerar relatórios sobre o estoque de produtos
def gerar_relatorios():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'RELATÓRIOS':^20}' + '—' * 20)

    # Calcula e exibe valor total em estoque (preço x quantidade de cada produto)
    valor_total = sum(p['preco'] * p['quantidade'] for p in BANCO_DADOS)
    print(f'\nValor total em estoque: R$ {valor_total:.2f}')

    # Define o limite para considerar um estoque como baixo
    estoque_baixo = 15
    # Filtra produtos com estoque abaixo do limite
    produtos_baixo = [p for p in BANCO_DADOS if p['quantidade'] < estoque_baixo]

    # Exibe o relatório de produtos com estoque baixo
    print(f'\nProdutos com estoque baixo(Abaixo de {estoque_baixo} unidades):')
    if not produtos_baixo:
        print('Não há produtos com estoque baixo.')
    else:
        # Exibe informações de cada produto com estoque baixo
        for produto in produtos_baixo:
            print(f"""
    Nome: {produto['nome']}
    Quantidade atual: {produto['quantidade']}
    Categoria: {produto['categoria']}""")


# Função para aplicar descontos em produtos de uma categoria específica
def aplicar_desconto():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'APLICAR DESCONTO':^20}' + '—' * 20)
    # Exibe as categorias disponíveis
    print('\nCategorias disponíveis:')
    for i, cat in enumerate(categorias_validas, 1):
        print(f'{i}. {cat}')

    try:
        # Solicita a categoria para aplicar o desconto
        cat_num = int(input('\nEscolha o número da categoria: '))
        # Verifica se a categoria escolhida é válida
        if not 1 <= cat_num <= len(categorias_validas):
            print('Categoria inválida!')
            return

        # Solicita o percentual de desconto
        percentual = float(input('Digite o percentual de desconto (1-100): '))
        # Verifica se o percentual está dentro do intervalo válido
        if not 0 < percentual <= 100:
            print('Percentual inválido!')
            return

        # Obtém o nome da categoria a partir do número escolhido
        categoria = categorias_validas[cat_num - 1]
        # Filtra os produtos da categoria escolhida
        produtos_categoria = [p for p in BANCO_DADOS if p['categoria'] == categoria]

        # Verifica se existem produtos na categoria
        if not produtos_categoria:
            print(f'Nenhum produto encontrado na categoria {categoria}')
            return

        # Para cada produto da categoria, calcula e oferece o desconto
        for produto in produtos_categoria:
            # Calcula o valor do desconto
            desconto = produto['preco'] * (percentual / 100)
            # Calcula o novo preço com desconto
            preco_com_desconto = produto['preco'] - desconto

            # Exibe as informações do produto e do desconto
            print(f"\n{produto['nome']}:")
            print(f"Preço original: R$ {produto['preco']:.2f}")
            print(f"Com desconto ({percentual}%): R$ {preco_com_desconto:.2f}")

            # Solicita confirmação para aplicar o desconto
            confirmacao = input('\nAplicar desconto? (S/N): ').upper()
            if confirmacao == 'S':
                # Atualiza o preço do produto com o desconto
                produto['preco'] = preco_com_desconto
                print('Desconto aplicado com sucesso!')
            else:
                print('Desconto não aplicado.')

    except ValueError:
        # Tratamento de erro para entradas não numéricas
        print('Digite valores numéricos válidos!')


# Área de execução principal do programa
# Este é o ponto de entrada do sistema, onde o menu principal é exibido e o usuário pode escolher
# qual funcionalidade deseja utilizar. O programa permanece em execução até que o usuário escolha sair.

while True:
    # Exibe o cabeçalho do menu principal com todas as opções disponíveis
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
    # Solicita ao usuário que escolha uma opção do menu
    opcao_escolhida = int(input('Digite sua opção: '))

    # Verifica qual opção foi escolhida e chama a função correspondente
    if opcao_escolhida == 1:
        # Chama a função para cadastrar um novo produto
        cadastrar_produto()
    elif opcao_escolhida == 2:
        # Chama a função para atualizar um produto existente
        atualizar_produto()
    elif opcao_escolhida == 3:
        # Chama a função para remover um produto
        remover_produto()
    elif opcao_escolhida == 4:
        # Chama a função para listar produtos com opções de filtragem e ordenação
        listar_produto()
    elif opcao_escolhida == 5:
        # Chama a função para buscar produtos específicos
        buscar_produto()
    elif opcao_escolhida == 6:
        # Chama a função para gerar relatórios sobre o estoque
        gerar_relatorios()
    elif opcao_escolhida == 7:
        # Chama a função para registrar vendas de produtos
        vender_produto()
    elif opcao_escolhida == 8:
        # Chama a função para aplicar descontos em produtos
        aplicar_desconto()
    elif opcao_escolhida == 0:
        # Encerra o programa
        print('Desligando o sistema...')
        break
    else:
        # Exibe mensagem de erro para opções inválidas
        print('Opção inválida.')
