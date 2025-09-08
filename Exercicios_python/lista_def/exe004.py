from datetime import timedelta
def calcula_viagem(saida, tempo, fuso):
    cont_hora = 0
    cont = 0
    while (cont < tempo):
        cont_hora += 1
        cont += 1

    hora = (saida+cont_hora)-fuso

    if(fuso<0):
        if((saida+cont_hora)-fuso > 24):
            hora = ((saida+cont_hora)-fuso) - 23
        print(hora)
    else:
        if((saida+cont_hora)+fuso > 24):
            hora = ((saida+cont_hora)-fuso) - 23
        print(hora)




s, t, f = input("").split()
s = int(s)
t = int(t)
f = int(f)

calcula_viagem(s,t,f)