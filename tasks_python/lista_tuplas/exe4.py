def main():
    numeros = []

    while True:
        numero = int(input('Digite um número inteiro (ou 0 para parar): '))
        if numero == 0:
            break
        numeros.append(numero)

    repetidos = set()
    vistos = set()

    for numero in numeros:
        if numero in vistos:
            repetidos.add(numero)
        else:
            vistos.add(numero)

    if repetidos:
        print(f'Números repetidos: {sorted(repetidos)}')
    else:
        print('Não existem números repetidos nesta lista.')

main()
