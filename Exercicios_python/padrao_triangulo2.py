"""

3. Obtenha uma quantidade de linhas, portanto um número inteiro maior do que 0, via entrada do usuário e exiba um triângulo simples formado pelo caractere * contendo a quantidade de linhas informada pelo usuário. Exemplo para quantidade de linhas = 4:
*
* *
* * *
* * * *



"""







qt = int(input("Digite a quantidade de linhas: "))
ast = '*'

linha = 1
while linha <= qt:
    coluna = 1
    while coluna <= linha:
        print(ast, end=" ")
        coluna += 1
    print()
    linha += 1
