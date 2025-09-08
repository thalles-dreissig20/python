"""1) Escreva um programa para aprovar o empréstimo bancário para compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela
não pode exceder 30% do salário ou então o empréstimo será negado. 


imovel = float(input("Valor da casa: "))
salario = float(input("Salario do comprador: "))
anos = int(input(("Em quantos anos: "))
prestacao = salario / (anos * 0.03)
if(prestacao < 30):
	print("Negado!!")
else:
	print("Aprovado!")

"""


"""3) Desenvolva um algoritmo que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status de acordo com:
Abaixo de 18,5 – abaixo do peso
Entre 18.5 e 25 – peso ideal
Entre 25 e 30 - sobrepeso
Entre 30 e 40 - obesidade
Acima de 40 - obesidade mórbida
Para o cálculo do IMC, considere: IMC = peso / (altura x altura) 


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
if(imc < 18,5):
	print("Abaixo do peso!")
elif(imc < 25):
	print("Peso ideal")
elif(imc < 30):
	print("Sobrepeso!")
elif(imc < 40):
	print("Obesidade")
else:
	print("Obesidade Morbida!!")
	
"""	


"""4) Faça um programa que leia 3 notas de um aluno, calcule sua média e mostre seu
conceito final conforme a indicação abaixo:
Abaixo de 5 – Reprovado
Entre 5 e menor que 7 – Em recuperação
Igual ou maior que 7 – Aprovado


nota1 = float(input(("Primeira nota: "))
nota2 = float(input(("Segunda nota: "))
nota3 = float(input(("Terçeira nota: "))
media = (nota1 + nota2 + nota3) / 2
if(media < 5):
	print("Reprovado!")
elif(media < 7):
	print("Em recuperação!")
else:
	print("Aprovado")
	
"""

"""
# Exercicio 1051

salario = float(input("Digite o salario: "))
if(salario <= 2000):
	print("Isento")
elif(2000 < salario <= 3000):
	salario = salario - 2000
	salario = salario * 0.8
	print("Imposto: {:.2f}".format(salario))
elif(3000 < salario <= 4500):
	i = 1000 * 0.08 
	salario = salario - 3000
	salario = i + (salario * 0.18)
	print("Imposto: {:.2f}".format(salario))
else: 
	i = 1000 * 0.08 + 1500 * 0.18
	salario = salario - 4500
	salario = i + (salario * 0.28)
	print("Imposto: {:.2f}".format(salario))
"""

"""
#Exercicio 1050

ddd = int(input("Digite o numero de discagem telefonica: "))
if(ddd == 61):
	print("Destino de Brasilia")
elif(ddd == 71):
	print("Destino de Salvador")
elif(ddd == 11):
	print("Destino de São Paulo")
elif(ddd == 21):
	print("Destino de Rio de Janeiro")
elif(ddd == 32):
	print("Destino de Juiz de Fora")
elif(ddd == 19):
	print("Destino de Campinas")
elif(ddd == 27):
	print("Destino de Vitoria")
elif(ddd == 31):
	print("Destino de Belo Horizonte")
else:
	print("DDD não cadastrado!")
	
"""

"""

#Exercicio 1052

mes = int(input("Digite um número de 1 a 12 para descobrir o mês: "))
if(mes == 1):
	print("January")
elif(mes == 2):
	print("February")
elif(mes == 3):
	print("March ")
elif(mes == 4):
	print("April ")
elif(mes == 5):
	print("May ")
elif(mes == 6):
	print("June ")
elif(mes == 7):
	print("July ")
elif(mes == 8):
	print("August ")
elif(mes == 9):
	print("September ")
elif(mes == 10):
	print("October ")
elif(mes == 11):
	print("November ")
elif(mes == 12):
	print("December ")
else:
	print("Valor Invalido!!")
	
"""
"""
#Exercicio 1036


valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: "))
delta = valorB**2 - 4*valorA*valorC
print("O valor de delta é: ", delta)
if(delta < 0):
	print("impossivel calcular!")
else:
	r1 = (- valorB - delta**0.5) / (2*valorA)
	r2 = (- valorB - delta**0.5) / (2*valorA)
	print("O valor de R1 é: ", r1)
	print("O valor de R2 é: ", r2)
"""
