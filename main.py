from datetime import datetime

# Sistema de Gerenciamento de Estoque e Vendas
# Este programa permite gerenciar produtos em estoque, realizar vendas,
# gerar relatórios e aplicar descontos por categoria.

# Lista para armazenar o histórico de vendas
HISTORICO_VENDAS = []

# Banco de dados inicial com produtos pré-cadastrados
# Cada produto possui: id, nome, preço, quantidade em estoque e categoria
BANCO_DADOS = [
    {'id': 'ABC-123', 'nome': 'Arroz Integral', 'preco': 15.99, 'quantidade': 50, 'categoria': 'Alimentos'},
    {'id': 'DEF-456', 'nome': 'Detergente Multiuso', 'preco': 8.50, 'quantidade': 30, 'categoria': 'Limpeza'},
    {'id': 'GHI-789', 'nome': 'Smartphone X', 'preco': 1299.99, 'quantidade': 10, 'categoria': 'Eletrônicos'},
    {'id': 'JKL-012', 'nome': 'Camiseta Basica', 'preco': 29.90, 'quantidade': 25, 'categoria': 'Vestuário'},
    {'id': 'MNO-345', 'nome': 'Feijao Premium', 'preco': 12.75, 'quantidade': 40, 'categoria': 'Alimentos'}
]

# Tupla com as categorias válidas para produtos
categorias_validas = ("Alimentos", "Limpeza", "Eletrônicos", "Vestuário")


#
#   Espaço reservado para funções auxiliares
#   Essas funções começam com _ que é a convenção utilizada em Python para indicar "uso interno"
#

# Função auxiliar para buscar um produto no banco de dados
# Parâmetros:
#   - chave: valor a ser buscado (id ou nome do produto)
#   - tipo: campo onde buscar (padrão é 'id')
# Retorna o produto encontrado ou None se não encontrar
def _buscar_produto(chave, tipo='id'):
    for produto in BANCO_DADOS:
        if produto[tipo] == chave:
            return produto
    return None


# Função auxiliar para verificar se um ID está no formato correto
# O formato válido é: 3 letras + hífen + 3 números (ex: ABC-123)
# Parâmetros:
#   - id: string com o ID a ser verificado
# Retorna True se o ID for válido, False caso contrário
def _verificar_id(id):
    # Divide o ID em duas partes usando o hífen como separador
    id_parts = id.strip().split('-')

    # Verifica se o ID tem exatamente duas partes
    if len(id_parts) != 2:
        print('Formato de ID inválido. Use o formato "ABC-123".')
        return False

    # Verifica se a primeira parte contém apenas letras
    if not id_parts[0].isalpha():
        print('A primeira parte do ID deve ser somente letras.')
        return False

    # Verifica se a primeira parte tem exatamente 3 letras
    if len(id_parts[0]) != 3:
        print('A primeira parte do ID deve ter somente 3 letras.')
        return False

    # Verifica se a segunda parte contém apenas números
    if not id_parts[1].isnumeric():
        print('A segunda parte do ID deve ser somente números.')
        return False

    # Verifica se a segunda parte tem exatamente 3 números
    if len(id_parts[1]) != 3:
        print('A segunda parte do ID ter somente 3 números.')
        return False

    # Se passou por todas as verificações, o ID é válido
    return True

#
#   Espaço reservado para funções principais
#   Essas funções são as que interagem com o usúario e por intermédio de funções internas e manipulação do BANCO_DADOS
#   gerenciam o sistema.
#

# Função para verificar se um produto com determinado ID já está cadastrado no sistema
# Parâmetros:
#   - produto_id: ID do produto a ser verificado
# Retorna True se o produto já estiver cadastrado, False caso contrário
def esta_cadastrado(produto_id):
    for produto in BANCO_DADOS:
        if produto['id'] == produto_id:
            return True
    return False


# Função para cadastrar um novo produto no sistema
# Solicita ao usuário todas as informações necessárias (ID, nome, preço, quantidade, categoria)
# Realiza validações para garantir que os dados inseridos são válidos
# Adiciona o produto ao banco de dados se todas as validações forem bem-sucedidas
def cadastrar_produto():
    # Declaração de variáveis globais para armazenar os dados do produto
    global id
    global nome
    global preco
    global quantidade
    global categoria

    # Loop para obter e validar o ID do produto
    while True:
        id = input('Digite o id do produto (Ex. ABC-123): ').upper()
        # Verifica se o ID está no formato correto
        if not _verificar_id(id):
            continue
        # Verifica se o ID já está cadastrado
        if esta_cadastrado(id):
            print('Esse ID já está cadastrado, escolha outro.')
            continue
        # Se chegar aqui significa que todas as condições estão corretas e pode ir para o proximo laço (while)
        break

    # Loop para obter e validar o nome do produto
    while True:
        nome = input('Digite o nome do produto: ').strip()
        # Verifica se o nome contém apenas caracteres alfanuméricos e espaços
        if nome.replace(' ', '').isalnum():
            break
        print('Nome inválido, use apenas letras, números e espaços.')

    # Loop para obter e validar o preço do produto
    while True:
        try:
            preco = float(input('Digite o preço do produto: R$ '))
            # Verifica se o preço é um valor positivo
            if preco > 0:
                break
            print('Preço inválido, digite um valor positivo.')
        except ValueError:
            print('Digite um valor numérico válido.')

    # Loop para obter e validar a quantidade do produto
    while True:
        try:
            quantidade = int(input('Digite a quantidade do produto: '))
            # Verifica se a quantidade é um valor positivo
            if quantidade > 0:
                break
            print('Quantidade inválida, digite um valor positivo maior que zero.')
        except ValueError:
            print('Digite um número inteiro válido.')

    # Loop para obter e validar a categoria do produto
    while True:
        # Exibe as categorias disponíveis
        print('\nCategorias disponíveis:')
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

    # Verifica se o produto já existe pelo nome (verificação adicional)
    if not esta_cadastrado(nome):
        # Adiciona o novo produto ao banco de dados
        BANCO_DADOS.append({'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade, 'categoria': categoria})
        print('Produto cadastrado com sucesso!')
    else:
        print('Produto já existe no banco de dados.')


# Função para atualizar informações de um produto existente
# Permite atualizar o preço, nome ou quantidade em estoque
def atualizar_produto():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'ATUALIZAR PRODUTO':^21}' + '—' * 19)

    # Solicita e valida o ID do produto
    id_local = input('Digite o ID do produto: ').upper()
    if not _verificar_id(id_local):
        return

    # Busca o produto pelo ID
    produto = _buscar_produto(id_local)
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

    # Exibe as opções de atualização
    print("""
    1. Atualizar preço
    2. Atualizar nome
    3. Atualizar quantidade
    """)

    try:
        # Obtém a opção escolhida pelo usuário
        opcao = int(input('Digite sua opção: ').strip())

        # Opção 1: Atualizar preço
        if opcao == 1:
            try:
                # Solicita e valida o novo preço
                novo_preco = float(input('Digite o novo preço: R$ '))
                if novo_preco > 0:
                    produto['preco'] = novo_preco
                    print('Preço atualizado com sucesso!')
                else:
                    print('Preço inválido. Digite um valor positivo.')
            except ValueError:
                print('Digite um valor numérico válido.')

        # Opção 2: Atualizar nome
        elif opcao == 2:
            # Solicita e valida o novo nome
            novo_nome = input('Digite o novo nome: ').strip()
            if novo_nome.replace(' ', '').isalnum():
                produto['nome'] = novo_nome
                print('Nome atualizado com sucesso!')
            else:
                print('Nome inválido, use apenas letras, números e espaços.')

        # Opção 3: Atualizar quantidade
        elif opcao == 3:
            try:
                # Solicita o ajuste de quantidade (adição ou remoção)
                ajuste = input('Digite a quantidade (use + ou - para ajustar) Ex. +10: ')

                # Adicionar ao estoque
                if ajuste.startswith('+'):
                    quantidade = int(ajuste[1:])
                    produto['quantidade'] += quantidade
                    print(f'Adicionadas {quantidade} unidades ao estoque.')

                # Remover do estoque
                elif ajuste.startswith('-'):
                    quantidade = int(ajuste[1:])
                    # Verifica se há quantidade suficiente
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

    # Solicita e valida o ID do produto
    id = input('Digite o ID do produto: ').upper()
    if not _verificar_id(id):
        return

    # Busca o produto pelo ID
    produto = _buscar_produto(id)
    if not produto:
        print('Produto não encontrado.')
        return

    # Verifica se o produto tem estoque
    if produto['quantidade'] == 0:
        print('Não é possível remover um produto sem estoque.')
        return

    # Solicita confirmação para remover o produto
    print(f"\nVocê realmente deseja remover {produto['nome']}? (S/N)")
    confirmacao = input().upper()

    # Remove o produto se confirmado
    if confirmacao == 'S':
        BANCO_DADOS.remove(produto)
        print('Produto removido com sucesso!')
    else:
        print('Operação cancelada.')


# Função para listar produtos com diversas opções de filtragem e ordenação
def listar_produto():
    # Define o limite para considerar estoque baixo
    estoque_baixo = 15

    # Exibe o cabeçalho e as opções disponíveis
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
        # Obtém a opção escolhida pelo usuário
        opcao = int(input('Digite sua opção: ').strip())

        # Cria uma cópia do banco de dados para não modificar o original
        produtos = BANCO_DADOS.copy()

        # Opção 1: Listar todos os produtos (não precisa filtrar)
        if opcao == 1:
            pass  # Lista todos

        # Opção 2: Filtrar por nome
        elif opcao == 2:
            nome = input('Digite o nome para filtrar: ').strip()
            # Filtra produtos que contêm o texto digitado no nome (case insensitive)
            produtos = [p for p in produtos if nome.lower() in p['nome'].lower()]

        # Opção 3: Filtrar por ID
        elif opcao == 3:
            id = input('Digite o ID para filtrar: ').upper()
            # Filtra produtos que contêm o texto digitado no ID
            produtos = [p for p in produtos if id in p['id']]

        # Opção 4: Filtrar por categoria
        elif opcao == 4:
            # Exibe as categorias disponíveis
            print('\nCategorias disponíveis:')
            for i, cat in enumerate(categorias_validas, 1):
                print(f'{i}. {cat}')

            # Solicita a categoria desejada
            cat_num = int(input('\nEscolha o número da categoria: '))
            if 1 <= cat_num <= len(categorias_validas):
                cat = categorias_validas[cat_num - 1]
                # Filtra produtos da categoria selecionada
                produtos = [p for p in produtos if p['categoria'] == cat]

        # Opção 5: Mostrar produtos com estoque baixo
        elif opcao == 5:
            # Filtra produtos com quantidade menor que o limite de estoque baixo
            produtos = [p for p in produtos if p['quantidade'] < estoque_baixo]

        # Opções 6, 7, 8: Ordenar produtos
        elif opcao in [6, 7, 8]:
            try:
                # Exibe as opções de ordenação
                print('—' * 21 + f'{'ORDENAR POR:':^18}' + '—' * 21 +
    '''
    1. Crescente
    2. Decrescente
    '''
                     )
                # Solicita a ordem desejada
                ordem = int(input("Digite sua opção: ").strip())

                # Valida a opção de ordenação
                if ordem not in [1, 2]:
                    print("Opção de ordenação inválida!")
                    return

                # Define se a ordenação será reversa ou não
                reverse = ordem == 2

                # Ordena de acordo com o campo selecionado
                if opcao == 6:
                    # Ordenar por nome
                    produtos.sort(key=lambda x: x['nome'], reverse=reverse)
                elif opcao == 7:
                    # Ordenar por preço
                    produtos.sort(key=lambda x: x['preco'], reverse=reverse)
                else:  # opcao == 8
                    # Ordenar por quantidade em estoque
                    produtos.sort(key=lambda x: x['quantidade'], reverse=reverse)
            except ValueError:
                print("Digite uma opção válida!")
                return
        else:
            print('Opção inválida!')
            return

        # Verifica se há produtos para exibir após a filtragem
        if not produtos:
            print('Nenhum produto encontrado!')
            return

        # Exibe as informações de cada produto
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


# Função para buscar produtos no sistema por diferentes critérios
def buscar_produto():
    # Exibe o cabeçalho e as opções de busca
    print('—' * 20 + f'{'BUSCAR PRODUTO':^20}' + '—' * 20 +
    """
    1. Buscar por ID
    2. Buscar por nome
    3. Buscar por categoria
    """)

    # Solicita e valida a opção de busca
    opcao_escolhida_busca = int(input('Digite sua opção:').strip())
    while opcao_escolhida_busca not in range(1, 4):
        print('Opção inválida.')
        opcao_escolhida_busca = int(input('Digite sua opção:').strip())

    # Variável global para armazenar os produtos encontrados
    global produtos

    # Opção 1: Buscar por ID
    if opcao_escolhida_busca == 1:
        # Solicita e valida o ID do produto
        id = str(input('Digite o ID do produto: '))
        while not _verificar_id(id):
            id = str(input('Digite o ID do produto: '))

        # Busca o produto pelo ID
        produto = _buscar_produto(id)
        if not produto:
            print('Não há nenhum produto com esse ID.')
            return

        # Armazena o produto encontrado em uma lista
        produtos = [produto]

    # Opção 2: Buscar por nome
    elif opcao_escolhida_busca == 2:
        # Solicita o nome do produto
        nome = input('Digite o nome do produto: ').strip()

        # Busca o produto pelo nome
        produto = _buscar_produto(nome, tipo='nome')
        if not produto:
            print('Não há nenhum produto com esse nome.')
            return

        # Armazena o produto encontrado em uma lista
        produtos = [produto]

    # Opção 3: Buscar por categoria
    elif opcao_escolhida_busca == 3:
        # Exibe as categorias disponíveis
        print('—' * 16 + f'{'CATEGORIAS DISPONÍVEIS':^28}' + '—' * 16 +
    """
    1. Alimentos
    2. Limpeza
    3. Eletrônicos
    4. Vestuário\n""")

        # Solicita e valida a categoria escolhida
        categoria_escolhida = int(input('Digite a categoria do produto: ').strip())
        print('')
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
        header = ('—' * 16 + f'{'INFORMAÇÕES DO PRODUTO':^28}' + '—' * 16)
        print(f"""{header}
    Identificador Unico(ID): {produto['id']}
    Nome: {produto['nome']}
    Preço: R$ {produto['preco']}
    Quantidade em Estoque: {produto['quantidade']}
    Categoria: {produto['categoria']}\n""")


# Função para registrar a venda de produtos
def vender_produto():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'VENDER PRODUTO':^20}' + '—' * 20)

    # Inicializa variáveis para controle da venda
    vendas_atuais = []  # Lista para armazenar as vendas realizadas na sessão atual
    valor_total_vendas = 0  # Valor total das vendas na sessão atual
    data_venda = datetime.now()  # Data e hora da venda

    # Loop para permitir vender múltiplos produtos em uma sessão
    while True:
        # Solicita e valida o ID do produto
        id = input('Digite o ID do produto: ').upper()
        if not _verificar_id(id):
            continue

        # Busca o produto pelo ID
        produto = _buscar_produto(id)
        if not produto:
            print('Produto não encontrado.')
            continue

        try:
            # Solicita e valida a quantidade desejada
            quantidade = int(input('Digite a quantidade desejada: '))
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

        # Calcula o valor total da venda
        total = produto['preco'] * quantidade

        # Solicita confirmação da venda
        print(f"\nConfirmar venda de {quantidade} unidade(s) de {produto['nome']}?")
        print(f"Valor total: R$ {total:.2f}")
        confirmacao = input("Digite S para confirmar: ").upper()

        # Se não confirmado, cancela esta venda específica
        if confirmacao != 'S':
            print('Venda cancelada.')
            continue

        # Atualiza o estoque e o valor total das vendas
        produto['quantidade'] -= quantidade
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

        # Pergunta se deseja vender mais produtos
        continuar = input("\nDeseja vender mais produtos? (S/N): ").upper()
        if continuar != 'S':
            break

    # Se houve vendas, gera um recibo
    if vendas_atuais:
        # Exibe o cabeçalho do recibo
        print('\n' + '—' * 24 + f'{'RECIBO':^12}' + '—' * 24)
        print(f"Data: {data_venda.strftime('%d/%m/%Y %H:%M:%S')}")
        print('—' * 60)
        print(f"{'Produto':<25} {'Qtd':>5} {'Valor Unit.':>12} {'Total':>12}")
        print('—' * 60)

        # Exibe os detalhes de cada item vendido
        for venda in vendas_atuais:
            print(
                f"{venda['produto']:<25} {venda['quantidade']:>5} {venda['valor_unitario']:>12.2f} {venda['valor_total']:>12.2f}")

        # Exibe o resumo da venda
        print('—' * 60)
        print(f"Total de itens vendidos: {len(vendas_atuais)}")
        print(f"Valor total da venda: R$ {valor_total_vendas:.2f}")


# Função para gerar relatórios sobre o estoque
def gerar_relatorios():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'RELATÓRIOS':^20}' + '—' * 20)

    # Calcula e exibe o valor total em estoque
    # Multiplica o preço pela quantidade de cada produto e soma todos os valores
    valor_total = sum(p['preco'] * p['quantidade'] for p in BANCO_DADOS)
    print(f'\nValor total em estoque: R$ {valor_total:.2f}')

    # Define o limite para considerar estoque baixo
    estoque_baixo = 15

    # Filtra produtos com estoque abaixo do limite
    produtos_baixo = [p for p in BANCO_DADOS if p['quantidade'] < estoque_baixo]

    # Exibe os produtos com estoque baixo
    print(f'\nProdutos com estoque baixo(Abaixo de {estoque_baixo} unidades):')
    if not produtos_baixo:
        print('Não há produtos com estoque baixo.')
    else:
        for produto in produtos_baixo:
            print(f"""
    Nome: {produto['nome']}
    Quantidade atual: {produto['quantidade']}
    Categoria: {produto['categoria']}""")


# Função para aplicar desconto em produtos de uma categoria específica
def aplicar_desconto():
    # Exibe o cabeçalho da função
    print('—' * 20 + f'{'APLICAR DESCONTO':^20}' + '—' * 20)

    # Exibe as categorias disponíveis
    print('\nCategorias disponíveis:')
    for i, cat in enumerate(categorias_validas, 1):
        print(f'{i}. {cat}')

    try:
        # Solicita e valida a categoria escolhida
        cat_num = int(input('\nEscolha o número da categoria: '))
        if not 1 <= cat_num <= len(categorias_validas):
            print('Categoria inválida!')
            return

        # Solicita e valida o percentual de desconto
        percentual = float(input('Digite o percentual de desconto (1-100): '))
        if not 0 < percentual <= 100:
            print('Percentual inválido!')
            return

        # Obtém o nome da categoria e filtra os produtos dessa categoria
        categoria = categorias_validas[cat_num - 1]
        produtos_categoria = [p for p in BANCO_DADOS if p['categoria'] == categoria]

        # Verifica se existem produtos na categoria selecionada
        if not produtos_categoria:
            print(f'Nenhum produto encontrado na categoria {categoria}')
            return

        # Para cada produto da categoria, calcula e aplica o desconto
        for produto in produtos_categoria:
            # Calcula o valor do desconto e o novo preço
            desconto = produto['preco'] * (percentual / 100)
            preco_com_desconto = produto['preco'] - desconto

            # Exibe as informações do desconto
            print(f"\n{produto['nome']}:")
            print(f"Preço original: R$ {produto['preco']:.2f}")
            print(f"Com desconto ({percentual}%): R$ {preco_com_desconto:.2f}")

            # Solicita confirmação para aplicar o desconto
            confirmacao = input('\nAplicar desconto? (S/N): ').upper()
            if confirmacao == 'S':
                produto['preco'] = preco_com_desconto
                print('Desconto aplicado com sucesso!')
            else:
                print('Desconto não aplicado.')

    except ValueError:
        print('Digite valores numéricos válidos!')


# Área de execução principal do programa
# É aqui que o Python vai executar o código principal para saber qual função chamar
# O programa funciona em um loop infinito até que o usuário escolha a opção de sair (0)

# Loop principal do programa
while True:
    # Exibe o menu principal com todas as opções disponíveis
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

    # Solicita a opção desejada pelo usuário
    opcao_escolhida = int(input('Digite sua opção: '))

    # Executa a função correspondente à opção escolhida
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
        # Chama a função para buscar produtos por diferentes critérios
        buscar_produto()
    elif opcao_escolhida == 6:
        # Chama a função para gerar relatórios sobre o estoque
        gerar_relatorios()
    elif opcao_escolhida == 7:
        # Chama a função para registrar vendas de produtos
        vender_produto()
    elif opcao_escolhida == 8:
        # Chama a função para aplicar descontos em produtos por categoria
        aplicar_desconto()
    elif opcao_escolhida == 0:
        # Encerra o programa
        print('Desligando o sistema...')
        break
    else:
        # Mensagem para opção inválida
        print('Opção inválida.')
