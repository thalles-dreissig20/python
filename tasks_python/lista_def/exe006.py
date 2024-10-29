def media(nota, cont):
    return nota / cont



nota = int(input())
total = 0
cont = 0
while nota >= 0:
    total += nota
    nota = int(input())

    cont += 1


print(media(total, cont))