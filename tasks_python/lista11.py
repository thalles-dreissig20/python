"""
#1533 - Detetive Watson
while True:
    n = int(input("Suspeitos: "))
    if(n == 0):
        break
    l = input().split()
    for i in range(n):
        l[i] = int(l[i])
       
    r = sorted(l, key=int)
    for ind, i in enumerate(l):
        if i == r[n-2]:
            print(ind+1)
            break
"""

"""
#2060 - Desafio de Bino
N = int(input("Quantidade de numeros na lista de BINO: "))
multiploDois = 0
multipleTres = 0
multipleQuatro = 0
multipleCinco = 0

values = input().split(' ')
valores = values[:N]
for i in range(N):
    valores[i] = int(valores[i])
    if(valores[i] % 2 ==0):
        multiploDois+=1
    if(valores[i] % 3 ==0):
        multipleTres+=1
    if(valores[i] % 4 ==0):
        multipleQuatro+=1
    if(valores[i] % 5 ==0):
        multipleCinco+=1
print('{0} Multiplo(s) de 2'.format(multiploDois))
print('{0} Multiplo(s) de 3'.format(multipleTres))     
print('{0} Multiplo(s) de 4'.format(multipleQuatro))     
print('{0} Multiplo(s) de 5'.format(multipleCinco)) 
"""
# Lista Composta/Matriz 
# a) Mostre a soma de todos os elementos pares da matriz 
# b) Mostre a média dos elementos da diagonal principal 
# c) Mostre o produto dos elementos da diagonal secundária 
# d) Mostre a média dos elementos acima da diagonal principal 
# e) Mostre a soma dos elementos da última coluna da matriz 
# f) Mostre o menor valor da primeira linha da matriz


matriz = [[0, 0, 0] [0, 0, 0] [0, 0, 0]]
soma_par = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite valor para a matriz: [{l}, {c}] "))
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        print()
print("Mostre a soma de todos os elementos pares da matriz: {}".format(soma_par))



"""
# 2)
from random import randint
from time import sleep

palpites = []
print('=' * 35 + f'\n{"PALPITE MEGA SENA":^35}\n' + '=' * 35)

quantidade_Jogos = int(input('Quantos jogos deseja: '))
print(f'\n{" > SORTEANDO VALORES < ":~^35}')
print()

for contagem in range(quantidade_Jogos):
    jogo = []
    for qtdValores in range(6):
        sorteio = randint(1, 60)

        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)

    jogo.sort()
    palpites.append(jogo[:])
    print(f'Jogo {contagem + 1}: {palpites[contagem]}')
    sleep(0.5)
print()
print(f'{" > BOA SORTE < ":~^35}')
"""


"""
# 3)
lista = [] 
while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Digite a 1° nota: '))
    nota2 = float(input('Digite a 2° nota: '))
    nota3 = float(input('Digite a 3° nota: ')) 
    lista_aluno = [nome, nota1, nota2, nota3]
    lista.append(lista_aluno)
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
        
print('-'*40) 
print('-=' *5,' Média dos alunos ','-='*5) 
print('-'*40)
print(f'{"NOME":^15} {"MÉDIA":>15}')
print('-'*40)
for pos,n in enumerate(lista):
    media = (n[1] + n[2] + n[3]) / 3
    print(f'{pos+1} > {n[0]:<15}{media:>10}')
print('-'*40)

while True:
    p = int(input('Mostrar notas de qual aluno? [999 para encerrar] '))
    if p == 999:
        print('Encerrando...')
        print('-=' *5,' Volte sempre! ','-='*5)  
        break
    if len(lista) >= p > 0:
        print(len(lista), p) 
        print(f'{lista[p-1][0]} tirou notas {lista[p-1][1]}, {lista[p-1][2]}, {lista[p-1][3]}')
    else:
        print('  Aluno não encontrado  ') 

"""