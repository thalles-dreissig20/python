"""
1) Escreva um programa que imprima todos os anos bissextos do século XXI.
Lembre-se que o primeiro ano bissexto do século foi em 2004 e que o último será
em 2096 e que os anos bissextos ocorrem usualmente de 4 em 4 anos

for i in range(2004,2097,4):
    print(i)

for i in range(2096,2003,-4):
    print(i)
    
"""
################################################################################
"""
2) Faça um programa que imprima na tela apenas os números ímpares entre 1 e
50.

for i in range(1,51):
    if((i%2)!=0):
        print(i)
    
"""
################################################################################
"""
3) Uma universidade particular oferece um desconto de 30% na mensalidade do
aluno com melhor nota (média geral). Implemente um programa que após
receber as informações do aluno (nome, nota/média geral, valor mensalidade)
verifique quem é o aluno com melhor nota e calcule o desconto de sua
mensalidade.
Ao final de sua execução, o programa deve mostrar:
- o nome do aluno com melhor nota,
- o valor da mensalidade (sem desconto) e
- o valor da mensalidade com o desconto e 30%;
Considerar 5 alunos (as informações devem ser lidas do teclado), considerar
alunos com notas distintas.


for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a media do aluno: "))
    mensalidade = float(input("digite a mensalidade: "))
    
    if(i==0):
        nome_aux = nome
        nota_aux = nota
        mensalidade_aux = mensalidade
    elif(nota > nota_aux):
        nota_aux = nota
        nome_aux = nome
        mensalidade_aux = mensalidade
print("O aluno com a maior nota: {}".format(nome_aux))
print("A mensalidade sem desconto: {}".format(mensalidade_aux))
print("A mensalidade com desconto de 30%: {}".format(mensalidade_aux * 0.7))

"""
################################################################################
"""
4) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
de números pares e a quantidade de números impares.

impar = 0
par = 0
for i in range(10):
    numero = int(input("digite um numero: "))
    if((numero%2)!=0):
        impar = impar + 1
    else:
        par = par + 1

print("A quantidade de par: {}". format(par))
print("A quantidade de impar: {}".format(impar))

"""
################################################################################
"""
5) Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1.

cont=0
num = int(input("Digite um numero para saber se e primo: "))
for i in range(1,num+1):
    if(num%i)==0:
        cont +=1
if cont ==2:
    print("Primo")
else:
    print("Nao Primo")
"""
################################################################################
"""
6) Altere o programa de cálculo dos números primos (exercício 5), informando,
caso o número não seja primo, por qual(is) número(s) ele é divisível.


cont=0
num = int(input("Digite um numero para saber se e primo: "))
for i in range(1,num+1):
    if(num%i)==0:
        cont +=1
if cont ==2:
    print("Primo")
else:
    print("Nao Primo")
    for i in range(1, num+1):
        if(num%i)==0:
            print(i)
            
"""
################################################################################
"""
7) Faça um programa que peça para n pessoas a sua idade (o valor de n será
solicitado ao usuário), ao final o programa deverá verificar se a média de idade
da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é
jovem, adulta ou idosa, conforme a média calculada.


soma = 0
pessoas = int(input("Quantas pessoas tem na turma? "))
for i in range(1, pessoas+1):
    idade = int(input("Qual a sua idade? "))
    soma = idade
    media = pessoas / soma
    
if(media <= 25):
    print("A turma e jovem")
elif(media <= 60):
    print("A turma e adulta")
else:
    print("A turma e idosa")
"""
################################################################################
"""
8) Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles. No final mostre a soma dos
números (do intervalo)


n1 = int(input('Infomer um numero inteiro: '))
n2 = int(input('Infomer outro numero inteiro: '))
soma = 0
if n1 > n2:
    for a in range(n2+1,n1):
        print(a)
        soma = soma + a

elif n1 < n2:
    for a in range(n1+1,n2):
        print(a)
        soma = soma + a
else:
    print('Os numeros são iguais.')
print(f'A soma dos numeros foi de {soma}')
"""

##############################################################################
"""
9) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja
ver a tabuada. 

num = int(input("Digite um numero para ver a tabuada: "))
for c in range(1, 11):
    print(' {} x {:2} = {}'.format(num, c, num*c))
"""
###############################################################################
"""
10) Considerar uma turma da Disciplina de Cálculo I, com 5 alunos, fazer um
programa que:


for i in range(5):
"""
###############################################################################
"""
11) Crie um programa que leia n números inteiros pelo teclado. No final da execução,
mostre a média entre os números lidos, qual foi o maior, e o menor valor lido.


num = int(input('Infome um número: '))
maior = num
soma = num
for i in range(5):
    num = int(input('Infome um número: '))
    soma += num
if num > maior:
    maior = num

media = soma/5
print('Maior: ', maior)
print('Soma: ', soma)
print('Média: ', media)
"""
###############################################################################
"""
12) Florianópolis é uma cidade que possui diversas praias.
De forma a melhor orientar os turistas a Secretaria Municipal de Turismo mediu
a distância de cada praia a partir do centro da cidade.
Seu programa deve solicitar que o usuário indique o número de praias que deseja
cadastrar. E para cada praia, indique o nome (string) e a distância do centro da
cidade (int).
A partir destas informações, seu programa deve obter os seguintes dados:
• qual a praia mais distante do centro da cidade;
• quantas praias estão entre 15 e 20 km do centro;
• qual a distância média das praias (arredondado na primeira casa decimal).
"""
