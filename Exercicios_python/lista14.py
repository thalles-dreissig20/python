## Exercicio 1281:
"""
N = int(input('Quantas vezes Parcinova foi à feira: '))  # número de casos de teste

produtos = [{'nome': 'mamao' , 'preco': 2.19},
            {'nome': 'cebola', 'preco': 3.10},
            {'nome': 'tomate', 'preco': 2.80},
            {'nome': 'uva', 'preco': 2.73}]

for ida in range(N):
    
    M = int(input('Quantos produtos estão disponíveis? '))
    #produtos = []

    for i in range(M):
        # preenche uma lista de dicionários, com nome e preço dos produtos da feira
        produto = input(f'Produto {i} - Nome e preço: ').split()
        info = {'nome': produto[0], 'preco': float(produto[1])}
        produtos.append(info.copy())
    

    P = int(input('Quantos produtos Parcinova quer comprar? '))
    comprou = []
    
    for e in produtos:
        for v in e.values():
            print(v, end=' ')
        print()
    
    for i in range(P):  # lista de dicionários, com nome e quantidade dos produtos a ser comprados
        produto = input(f'Produto {i} - Nome e quantidade: ').split()
        info = {'nome': produto[0], 'quantidade': int(produto[1])}
        comprou.append(info.copy())
    
    valorCompra = 0  # determina o valor final da compra
    for c in comprou:  # percorre a lista de itens comprados
        for p in produtos: # percorre a lista de produtos disponíveis na feira
            if c['nome'] == p['nome']:  # encontra, pelo nome, o produto comprado
                valorCompra += c['quantidade'] * p['preco']  # multiplica a quantidade comprada pelo preço e
                                                             # acumula esse valor com os valores prévios
    
    print('R$:', valorCompra)
"""
###############################################################################################################################################
## Exercicio 2482
"""
numeroTraducao = int(input("Quantas traduções: "))
dict = {}
while numeroTraducao:
    numeroTraducao -= 1
    lingua = input("Linguagem: ")
    trad = input("Tradução: ")
    dict[lingua] = trad

numeroPessoas = int(input("Quantidade de pessoas: "))
while numeroPessoas:
    numeroPessoas -= 1
    pessoa = input("Nome: ")
    lingua = input("Linguagem: ")
    print("")
    print(pessoa)
    print(dict[lingua])
    print()
"""
###############################################################################################################################################
## Exercicio 1911
"""
numEstudante = 1
while True:
    numEstudante = int(input("Numero de estudantes: "))
    if numEstudante == 0: break

    dic = {}

    for x in range(numEstudante):
        assinatura = input("Nome/Assinatura: ").split()
        dic[assinatura[0]] = assinatura[1]

    aluno = int(input("Presença de aluno: "))
    nome, ass = int(0), int(0)

    for x in range(aluno):
        count = int(0)
        name_dic = input("Nome/Assinatura: ").split()
        for y in dic[name_dic[0]]:
            if y != name_dic[1][count]:
                nome += 1
            count += 1
        if nome > 1: ass += 1

        nome = 0

    print(ass)
"""
#############################################################################################################################################
## Exercicio 1763

# brasil   Feliz Natal!
# inglaterra Feliz Natal!
# Áustria Feliz Natal!
# coreia              Chuk Sung Tan!
# espanha             Feliz Navidad!
# A Grécia de Kala Christougen!
# estados-unidos      Merry Christmas!
# inglaterra          Merry Christmas!
# austrália Feliz Natal!
# portugal            Feliz Natal!
# Suecia Feliz Natal!
# turquia feliz natal
# argentina           Feliz Navidad!
# chile               Feliz Navidad!
# mexico              Feliz Navidad!
# Antardida Feliz Natal!
# Canadá Feliz Natal!
# Irlanda Feliz Natal!
# Bélgica Feliz Natal!
# Itália Feliz Natal!
# Líbia Feliz Natal!
# siria Milad Mubarak!
# marrocos            Milad Mubarak!
# japao Merii Kurisumasu!
"""
bancodeDados = {'brasil':'Feliz Natal!',
                'alemanha':'Frohliche Weihnachten!',
                'austria':'Frohe Weihnacht!',
                'coreia':'Chuk Sung Tan!',
                'espanha':'Feliz Navidad!',
                'grecia':'Kala Christougena!',
                'estados-unidos':'Merry Christmas!',
                'inglaterra':'Merry Christmas!',
                'australia':'Merry Christmas!',
                'portugal':'Feliz Natal!',
                'suecia':'God Jul!',
                'turquia':'Mutlu Noeller',
                'argentina':'Feliz Navidad!',
                'chile':'Feliz Navidad!',
                'mexico':'Feliz Navidad!',
                'antardida':'Merry Christmas!',
                'canada':'Merry Christmas!',
                'irlanda':'Nollaig Shona Dhuit!',
                'belgica':'Zalig Kerstfeest!',
                'italia':'Buon Natale!',
                'libia':'Buon Natale!',
                'siria':'Milad Mubarak!',
                'marrocos':'Milad Mubarak!',
                'japao':'Merii Kurisumasu!'}

a = str(input("Pais: ")).lower()
if a == '':
    print("Nenhum Pais encontrado!")
elif a in bancodeDados:
    print(bancodeDados[a])
else:
    print("---NOT FOUND!---")
"""
        
###########################################################################################################################################
## Exercicio 1430


###########################################################################################################################################
## Exercicio 2091
"""
numeros = {}
casosdeteste = int(input("Quantos números: "))
for i in range(casosdeteste):
    numero = int(input("digite os números: ")).split()
    if numero < 1 and numero > 10:
        print("numeros invalidos!")
    else:
        numeros.append(numero.copy())
"""


frutas = {'mamao': 2.19,
          'cebola': 3.10,
          'tomate': 2.80,
           'uva': 2.73}

while True:
    print('Cadastrando frutas...')
    
    continua = input("Deseja cadastrar?")
    if continua == 'N':
        break

    nome = input("digite a fruta:")
    preco = input("Digite o valor")
    frutas[nome] = preco
   
    

#carrinho de compras
n = int(input("qual quantidade de compras?"))
total=0
for i in range(n):
    produto = input('digite a fruta: ')
    qtd = int(input("Digite a quantidade: "))
    
    for k,v in frutas.items():
        if produto == k:
            total = total + (qtd * v)
    print(total)
