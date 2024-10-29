'''
1 1 0 1 0
0 0 1 0 1
'''

def listaCompativel(conector1, conector2):
    intConector1 = list(map(int, conector1))
    intConector2 = list(map(int, conector2))
    lista = []
    cont = 0
    while(cont < 5):
        a = intConector1[cont]
        b = intConector2[cont]
        if ((a + b) == 1):
            lista.append(1)
        else:
            return 'N'
        cont += 1
    return 'Y'

conectores = 2
conector1 = []
conector2 = []
for i in range(0, conectores):
    if i == 0:
        conector1 = input().split(' ')
    else:
        conector2 = input().split(' ')

res = listaCompativel(conector1, conector2)
print(res)