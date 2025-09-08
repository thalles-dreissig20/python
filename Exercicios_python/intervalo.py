def verificaIntervalo(inicio, fim, num, param):
    if(param == False):
        if(num < fim and num > inicio):
            return True
        else:
            return False
    else:
        if(num <= fim and num >= inicio):
            return True
        else:
            return False


res = verificaIntervalo(0, 20, 20, False)
print(res)