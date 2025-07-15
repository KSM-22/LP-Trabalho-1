# LP_Trabalho_1

Projeto 1 da disciplina de Laboratório de Programação.<br>
1º Semestre do curso
de [Análise e Desenvolvimento de Sistemas](https://www.ufc.br/ensino/guia-de-profissoes/17805-analise-e-desenvolvimento-de-sistemas)

Equipe: Jhefferson e Pablo.

# Restrição técnica

Não pode utilizar _imports_ ou bibliotecas.

# Enunciado

## Cadastro de produtos

### Adicionar produto:

○ ID (formato "ABC-123", onde ABC são 3 letras e 123 são 3 números).
<br>○ Nome (sem caracteres especiais, apenas letras, números e espaços).
<br>○ Preço (positivo, com validação para números decimais).
<br>○ Quantidade (inteiro positivo, não pode ser zero no cadastro).
<br>○ Categoria (fixas: "Alimentos", "Limpeza", "Eletrônicos", "Vestuário").

### Verificações:

○ Se o produto já existe antes de cadastrar.
<br>○ ID único (não pode repetir).
<br>○ Nome com no mínimo 3 caracteres.

## Atualização de produtos:

### Alterar informações:

○ Campos editáveis: preço, descrição, quantidade.

### Aumentar/diminuir estoque (entrada/saída de produtos).

Exemplo:
<br>○ +5 aumenta a quantidade.
<br>○ -3 diminui (se houver estoque suficiente).
<br>● Se quantidade for atualizada para zero, alertar "estoque esgotado".

## Exclusão de Produtos

Remover produto do sistema:
<br>○ Confirmação obrigatória: "Você realmente deseja remover [Nome do
Produto]? (S/N)".
<br>○ Impedir exclusão se o produto estiver sem estoque.

## Busca e listagem:

● Listar todos os produtos.
<br>● Buscar por:
<br>○ Nome;
<br>○ ID; ou
<br>○ Categoria.
<br>● Filtrar produtos com estoque baixo (abaixo de um limite definido, a critério do aluno).

## Validação de dados:

● Impedir entrada inválida:
<br>○ Preço negativo ou zero.
<br>○ Quantidade não numérica.
<br>○ Categoria inexistente.

## Interface de usuário (CLI ou GUI)

● Menu interativo no terminal (input + loops).
<br>● Exemplo de interface de usuário com Menu interativo (CLI):

```text
=== MENU PRINCIPAL ===
1. Cadastrar produto
2. Atualizar produto
3. Remover produto
4. Listar produtos (ordenar por: nome/preço/estoque)
5. Buscar produto
6. Relatórios (Valor total/Estoque baixo)
7. Vender produto
8. Aplicar desconto
0. Sair
```

## BÔNUS

### Descontos/Promoções:

● Aplicar descontos em produtos:
<br>○ Definir uma promoção (ex.: "10% de desconto em produtos da categoria
'Limpeza'").
<br>○ Mostrar preço original e com desconto na listagem.
<br>■ Preço original: R\$ 50 → Com desconto: R\$ 45.

### Vender produto: permitir que o usuário "venda" produtos, diminuindo o estoque.

#### Fluxo:

1. Buscar produto por ID.
2. Verificar estoque.
3. Registrar venda (diminuir estoque).
4. Gerar recibo com: Nome do produto, quantidade, preço unitário, total.
   <br>● Histórico de vendas: Lista com data, produto, quantidade vendida.
   <br>● Registrar histórico de vendas (em uma lista separada).

#### Ordenação de produtos:

● Permitir ordenar a lista por:
<br>○ Nome (A-Z).
<br>○ Preço (do mais barato ao mais caro).
<br>○ Quantidade em estoque (do menor para o maior).
