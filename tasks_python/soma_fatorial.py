"""
2. Obtenha uma quantidade de números a serem lidos via entrada do usuário (qt). Em seguida, obtenha essa quantidade de números (qt) via entrada e, ao final, exiba o somatório dos fatoriais dos números lidos.

"""


qt = int(input("Digite a quantidade de números a serem lidos: "))
soma_fatoriais = 0

count = 0
while count < qt:
    numero = int(input())
    
    fatorial = 1
    i = 1
    while i <= numero:
        fatorial *= i
        i += 1
    
    soma_fatoriais += fatorial
    count += 1

print(soma_fatoriais)
