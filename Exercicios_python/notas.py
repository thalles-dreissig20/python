def verificaNotas(nota):
    if(nota <= 10 and nota >= 0):
        return True
    else:
        return False
    



verificaNota = verificaNotas(11)
print(verificaNota)