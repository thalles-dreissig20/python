import random

def main():
    numeros = [random.randint(1, 100) for _ in range(5)]
    
    print(f'Números gerados: {numeros}')
    
    maior = numeros[0]
    menor = numeros[0]
    
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    print(f'Maior número: {maior}')
    print(f'Menor número: {menor}')

main()
