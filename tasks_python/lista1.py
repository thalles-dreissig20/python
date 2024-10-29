def retornaLista(lista):
    listaNova = []
    tam = len(lista)
    maior = max(lista)
    cont = 0
    while cont < tam:
        listaNova.append(lista[cont] / maior)
        print(cont/maior)
        cont = cont + 1
    return listaNova


lista = [1,4,9]
res = retornaLista(lista)

print(res)