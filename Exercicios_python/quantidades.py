num_pares = 0
num_impares = 0
maior_impar = None

while True:
    numero = int(input())
    
    if numero < 0:
        break

    if numero % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
        if maior_impar is None or numero > maior_impar:
            maior_impar = numero

print(f'{num_pares}, {num_impares}, {maior_impar if maior_impar is not None else "nenhum"}')
