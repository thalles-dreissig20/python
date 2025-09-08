'''
5

0 1
1 2
1 2
0 2
1 1

'''

def resultadoMinas(minas):
    lista_de_minas = list(map(int, minas))

    lista_resultado = []
    cont = 0
    while(cont < len(lista_de_minas)):
        a = 0
        if (cont == 0):
            a += lista_de_minas[cont]
            a += lista_de_minas[cont+1]

        elif(cont > 0 and cont < (len(lista_de_minas)-1)):
            a += lista_de_minas[cont]
            a += lista_de_minas[cont+1]
            a += lista_de_minas[cont-1]

        else:
            a += lista_de_minas[cont]
            a += lista_de_minas[cont-1]
        
        lista_resultado.append(a)
        cont += 1

    return lista_resultado


minas = []
minas = input().split(' ')

res = resultadoMinas(minas)
print(res)