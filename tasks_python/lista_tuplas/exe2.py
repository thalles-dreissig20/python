def main():
    numeros = []
    contagem_nove = 0
    primeiro_tres_posicao = -1
    numeros_pares = []

    for i in range(5):
        numero = int(input(f'Digite o {i+1}º número: '))
        numeros.append(numero)

        if numero == 9:
            contagem_nove += 1
        
        if numero == 3 and primeiro_tres_posicao == -1:
            primeiro_tres_posicao = i

        if numero % 2 == 0:
            numeros_pares.append(numero)

    print(f'\nO número 9 apareceu {contagem_nove} vezes.')
    
    if primeiro_tres_posicao != -1:
        print(f'O primeiro valor 3 foi digitado na posição {primeiro_tres_posicao}.')
    else:
        print('O número 3 não foi digitado.')
    
    print(f'Números pares digitados: {numeros_pares}')

main()
