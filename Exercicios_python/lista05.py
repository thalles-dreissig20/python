#Exercicio 1113
"""
x, y = [int(x) for x in input("Digite dois valores inteiro, um ao lado do outro separados por espaço: ").split()]
if(x < y):
    print("Crescente!")
elif(x > y):
    print("Decrescente!")
else:
    print("")
elif:
    ()
elif:
    ()
elif:
    ()
"""
#########################################################################################################################################################
"""
#Exercicio 1099 - Não acabado
soma = 0
testes = int(input("Quantas vazes: "))
while(soma < testes):
    x, y = [int(x) for x in input("Digite dois valores inteiro, um ao lado do outro separados por espaço: ").split()] 
    
"""
######################################################################################################################################################
#Exercicio 1021
"""
valor = float(input("valor: "))
cem_r = int(valor // 100)
valor %= 100
cinquenta_r = int(valor // 50)
valor %= 50
vinte_r = int(valor // 20)
valor %= 20
dez_r = int(valor // 10)
valor %= 10
cinco_r = int(valor // 5)
valor %= 5
dois_r = int(valor // 2)
valor %= 2
um_r = int(valor // 1)
valor %= 1
cinquenta_c = int(valor // 0.50)
valor %= 0.50
vintecinco_c = int(valor // 0.25)
valor %= 0.25
dez_c = int(valor // 0.10)
valor %= 0.104
cinco_c = int(valor // 0.05)
valor %= 0.05
um_c = int(valor // 0.01)
print("NOTAS: \n{} nota(s) de R$ 100.00 \n{} nota(s) de R$ 50.00 \n{} nota(s) de R$ 20.00 \n{} nota(s) de R$ 10.00 \n{} nota(s) de R$ 5.00 \n{} nota(s) de R$ 2.00".format(cem_r, cinquenta_r, vinte_r, dez_r, cinco_r,dois_r))
print("MOEDAS: \n{} moeda(s) de R$ 1.00 \n{} moeda(s) de R$ 0.50 \n{} moeda(s) de R$ 0.25 \n{} moeda(s) de R$ 0.10 \n{} moeda(s) de R$ 0.05 \n{} moeda(s) de R$ 0.01".format(um_r,cinquenta_c, vintecinco_c, dez_c,cinco_c, um_c))
"""
########################################################################################
#Exercicio 17
"""
pedra = 0
papel = 1
tesoura = 2
jogar_novamente = "Sim"
while (jogar_novamente == "Sim"):
    jogador1 = int( input("Jogador1, digite 0 p/pedra, 1 p/papel ou 2/tesoura: " ))
    jogador2 = int( input("Jogador2, digite 0 p/pedra, 1 p/papel ou 2/tesoura: " ))
    if (0 <= jogador1 <= 2) and (0 <= jogador2 <= 2):
        if (jogador1 == jogador2):
            print("Empate! Ninguém ganhou." )
        elif (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
            print("Jogador 1 ganhou." )
        else:
            print("Jogador 2 ganhou." )
    else:
        print("Opção inválida." )
    jogar_novamente = input("Você quer tentar novamente? Digite Sim ou Não: " )
print("Até a próxima!" )
"""
##########################################################################################
#Exercicio 18
"""
a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))

if a >= b and a >= c and b >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
elif a >= b and a >=c and c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
elif b >= a and b >= c and a >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
elif b >= a and b >= c and c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
elif c >= a and c >= b and a >=b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
elif c >= a and c >= b and b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')
"""
#########################################################################################
#Exercicio 19
"""
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c) :
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')
"""


