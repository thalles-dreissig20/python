def printarLista(lista):
    cont = 0
    while(cont < len(lista)):
        a = 0
        if(lista[cont] > 0):
            a = lista[cont]
            print(f"X[{cont}] = {a}")
            cont += 1


lista = [0, -5, 63, -3, 2, -10]
res = printarLista(lista)