"""
1. Obtenha via entrada do usuário dois números inteiros positivos quaisquer (início e fim) e exiba as tabuadas dos números presentes no intervalo entre início e fim (incluindo esses números). Apresente da seguinte forma (exemplo com os números 2 e 6 como entrada):
Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
…
2 x 10 = 20
Tabuada do 3:
3 x 1 = 3
… 
3 x 10 = 30
…
Tabuada do 6:
…

"""


inicio = int(input())
fim = int(input())

num = inicio

while num <= fim:
    print(f'Tabuada do {num}:')
    i = 1
    while i <= 10:
        resultado = num * i
        print(f'{num} x {i} = {resultado}')
        i += 1
    num += 1
