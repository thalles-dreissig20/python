def jogo_paula(num):
    cont = 0
    while(cont <= num):
        cont += 1
        primeiro, segundo, terceiro = input().split()
        primeiro = int(primeiro)
        terceiro = int(terceiro)
        if(segundo.upper() == segundo):
            return primeiro - terceiro
        else:
            return primeiro + terceiro



num = int(input())
res = jogo_paula(num)
print(res)