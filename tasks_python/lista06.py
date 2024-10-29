#Exercicio 2057: fuso horario
"""
def fuso(hora, viagem, fuso):
    chegada = hora + viagem + fuso
    if(chegada > 24):
        chegada = chegada - 24
        print(chegada)
    elif(chegada < 0):
        chegada = chegada + 24
        print(chegada)
    else:
        print(chegada)

var = False
while (var == False):
    x, y, z = input("Digite 3 numeros: ").split()
    x = int(x)
    y = int(y)
    z = int(z)
    if(0<=x<=23 and 1<=y<=12 and -5<=z<=5):
        var = True
    else:
        var = False
fuso(x, y, z)
"""
#Exercicio 1150:
"""
def excedendo(x,z):
    soma = 0
    cont = 1
    while (soma <= z):
        soma = soma +x
        if (soma > z):
            break
        x = x+1
        cont = cont +1
    print(cont)
    
x, z = input("Digite x, z: ").split()
x = int(x)
z = int(z)

while (x >= z):
    z = int(input("Digite z novamente: "))
    
excedendo(x,z)
"""
################################################################
"""3) Faça um programa que leia 10 números inteiros do teclado, seu programa deve ter
uma função que verifique e retorne (a cada novo número digitado) se ele é par ou
ímpar. A partir desta informação, ao final de sua execução, seu programa deve
imprimir o número total de pares e ímpares que foram digitados"""
"""
def imparPar():
    contPar = 0
    contImpar = 0
    cont = 0
    for i in range(10):
        var = int(input("Digite um numero: "))
        cont +=1
        if((var%2)!=0):
            contImpar += 1
        else:
            contPar += 1
    return contPar, contImpar


par, impar = imparPar()
print("total de {} pares e {} impares".format(par, impar))
"""
###########################################################
"""
2) Considerar uma turma da Disciplina de Cálculo I, com 5 alunos, fazer um programa
que tenha uma função que calcule a média das notas da turma e verifique o aluno com
a melhor nota. Esta função deve retornar a média da turma e a nota do aluno com a
média mais alta.
No programa principal após conhecer o média mais alta, informe seu status (aprovado,
reprovado ou em recuperação). Para definir o status assuma a seguinte premissa:
Considerando que essas regras funcionam da mesma forma que funcionam na UFSC:
se a média for 5.75 ou maior, o aluno está aprovado, se o aluno não estiver aprovado
mas a nota for maior ou igual a 2.75, ele tem o direito de fazer a prova de recuperação
e se a média for menor que 2.75 ele está reprovado.
"""
"""
def media(turma, aluno):
    turma = 0
    aluno = 1
    media_alta = 0
    a, b, c, d, e = input("Digite as notas dos alunos separados por espaço: ").split()
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    media_turma = (a + b + c + d + e) / 5
    if(a > b, c, d, e):
        media_alta = a
        print("media mais alta {}".format(media_alta))
    elif(b > a, c, d, e):
        media_alta = b
        print("media mais alta {}".format(media_alta))
    elif(c > a, b, d, e):
        media_alta = c
        print("media mais alta {}".format(media_alta))
    elif(d > a, c, b, e):
        media_alta = d
        print("media mais alta {}".format(media_alta))
    else:
        media_alta = e
        print("media mais alta {}".format(media_alta))

aluno = 0
turma = 0
media(turma, aluno)
"""
###########################################################################
"""
Exercicio 1154
Escreva um algoritmo para ler um número não declarado de dados, cada um contendo a
idade de um indivíduo. Os dados finais, que não serão inseridos nos cálculos, contêm o valor
de uma idade negativa. Calcule e imprima a idade média desse grupo de indivíduos.
"""
"""
def media():
    media = 0
    cont = 0
    while(cont >= 0 ):
        idade = int(input("Digite sua idade: "))
        if(idade < 0):
            break
        else:
            media = media + idade
            cont += 1
    res = media / cont
    return res

res = media()
print(res)
"""
################################################################################
"""
Exercicio 1064
Leia 6 valores que podem ser números de ponto flutuante.
Depois, imprima quantos deles foram positivos. Na próxima linha,
imprima a média de todos os valores positivos digitados, com um dígito
após o ponto decimal.
"""
"""
def inteiro():
    contInteiro = 0
    cont = 0
    for i in range(6):
        num = float(input("Digite um numero: "))
        if(num > 0):
            contInteiro = contInteiro + num
            cont += 1
    res = contInteiro / cont
    return res, cont

res, cont = inteiro()
print("Você digitou {} números positivos!".format(cont))
print("Media dos numeros inteiros {}".format(res))
"""   