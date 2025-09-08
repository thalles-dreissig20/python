import random

def gerar_numeros_aleatorios(quantidade):
    numeros_aleatorios = []
    
    for _ in range(quantidade):
        numero = random.randint(1, 100) 
        numeros_aleatorios.append(numero)
    
    return numeros_aleatorios

quantidade_desejada = 10 
numeros_aleatorios = gerar_numeros_aleatorios(quantidade_desejada)
print(numeros_aleatorios)
