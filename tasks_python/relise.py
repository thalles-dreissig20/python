def funcao(a, b, c, h, l):
    if(a<=l or a<=h) and (b<=l or b<=h):
        colchao = "S"
    elif(a<=l or a<=h) and (c<=l or c<=h):
        colchao = "S"
    elif(b<=l or b<=h) and (c<=l or c<=h):
        colchao = "S"
    else:
        colchao = "N"
    return colchao

#Validação do colchão
validacao_colchao = False
while(validacao_colchao == False):
    a, b, c = input("dimensões do colchão: ").split()
    a = int(a)
    b = int(b)
    c = int(c)
    if(1<=a<=300 and 1<=b<=300 and 1<=c<=300):
        validacao_colchao = True
    else:
        validacao_colchao = False

#Validação da porta
validacao_porta = False
while(validacao_porta == False):
    h, l = input("Digite as dimencões da porta: ").split()
    h = int(h)
    l = int(l)
    if(1<=h<=250 and 1<=l<=250):
        validacao_porta = True
    else:
        validacao_porta = False

res = funcao(a, b, c, h, l)
print(res)
