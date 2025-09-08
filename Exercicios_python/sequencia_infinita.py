numero = int(input())

e_aproximado = 1.0
fatorial = 1

for i in range(1, numero):
    fatorial *= i
    e_aproximado += 1 / fatorial

print(e_aproximado)