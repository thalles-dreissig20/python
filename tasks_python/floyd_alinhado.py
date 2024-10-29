n = int(input("Digite o número de linhas para o Triângulo de Floyd: "))

num_digits = len(str(n * (n + 1) // 2))

contador = 1

for i in range(1, n + 1):
    for j in range(i):
        formatted_number = str(contador).zfill(num_digits)
        print(formatted_number, end=" ")
        contador += 1
    print()
