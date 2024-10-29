"""
1) Escreva um programa que leia o sexo das pessoas, mas somente aceite
“M” ou “F”. Caso esteja errado, peça a digitação novamente até ter um valor
correto.

sexo = input("Qual o seu sexo? [F] ou [M]: ").upper()
while (sexo == 'F' and sexo == 'M'):
    if(sexo == 'F'):
        print("Feminino")
    else:
        print("Masculino")
    break
else:
    print("Erro!")


"""
#####################################################################################
"""
2) Implemente um jogo onde o usuário deve adivinhar o número escolhido
pelo computador (entre 0 e 10). O Usuário irá digitando valores até descobrir
este valor. Quando o usuário “acertar”, uma mensagem avisa o final do jogo
(que o número correto foi digitado) e o número de tentativas.


from random import randrange
num = randrange(11)
cont = 1
teclado = int(input("DIgite um numero de 0 a 10: "))
while(num != teclado):
    teclado = int(input("Digite novamente:"))
    cont += 1
print("Parabens vc acertou o numero {} de {} tentativas".format(num, cont))
"""
#####################################################################################

#Exercicio 1075
"""
cont = 1
n = int(input("Digite um numero:"))

while (n < 1) or (n>100):
    n = int(input("Digite um numero valido: "))
    
while(cont <100):
    if (cont%n) ==2 :
        print(cont)
    cont += 1
"""
####################################################################################
#Exercicio 1078
"""
cont = 1
res = 0
n = int(input("Digite um numero: "))

while (n <= 1) or (n >= 1000):
    n = int(input("Digite um valor valido"))
while(cont < 11):
    res = cont * n
    print("{} X {} = {}".format(cont, n, res))
    cont += 1
"""
#####################################################################################
#Exercicio 1146
"""
cont = int(input("Digite um numero: ")) 
n = 1
while(n <= cont):
    print(n, end=' ')
    n += 1
"""
#####################################################################################
#Exercicio 1134
"""
cont= 0
alcool = 0
gasolina = 0
diesel = 0
while (cont > 1) or (cont <= 4):
    cont = int(input(" Alcool [1] \n Gasolina [2] \n Diesel [3] \n Fim [4] \n Tipo de combustivel:"))
    if(cont == 1):
        alcool += 1
    elif(cont == 2):
        gasolina += 1
    elif(cont == 3):
        diesel += 1
    else:
        print("Fim")
        break
print("MUITO OBRIGADO \n Alcool: {} \n Gasolina: {} \n diesel: {}".format(alcool, gasolina,diesel))
"""
######################################################################################
#Exercicio 1101
"""
n = 1
valorInicial = int(input("Digite um numero: "))
valorFinal = int(input("Digite outro numero: "))
while(n <= valorInicial):
    print(n, end=' ')
    n += 1
""" 











