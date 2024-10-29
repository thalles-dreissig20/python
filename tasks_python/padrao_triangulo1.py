"""
4. Mesmo enunciado do exercício anterior, porém com o seguinte padrão de triângulo (exemplo para entrada 4):
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 


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

linha = qt - 1
while linha >= 1:
    coluna = 1
    while coluna <= linha:
        print(ast, end=" ")
        coluna += 1
    print()
    linha -= 1