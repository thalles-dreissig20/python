def printarLista(n):
    cont = 0
    lista = []
    while(cont <= 10):
        lista.append(n)
        n += n
        cont += 1
    return lista

lista = printarLista(2)
index = 0
while(index < len(lista)):
    print(f"N[{index}] = {lista[index]}")
    index += 1