def verificaIntervalo(inicio, fim, num):
    if(num < fim and num > inicio):
        return True
    else:
        return False



res = verificaIntervalo(0, 20, 5)
print(res)