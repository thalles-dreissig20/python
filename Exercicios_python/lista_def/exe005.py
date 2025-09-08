def controlaElevador(saiu, entrou, capacidade_maxima, qtde_pessoas):
    controle = entrou
    controle -= saiu
    controle += qtde_pessoas

    if (controle > capacidade_maxima):
        return controle, 'S'
    else:
        return controle, 'N'
    



sensor, capacidade_maxima = input().split()
sensor = int(sensor)
capacidade_maxima = int(capacidade_maxima)

cont = 0
elevador_quebrou = None
qtde_pessoas = 0
a = 'N'

while (cont < sensor):
    cont += 1
    saiu, entrou = input().split()
    saiu = int(saiu)
    entrou = int(entrou)
    controle, elevador_quebrou = controlaElevador(saiu, entrou, capacidade_maxima, qtde_pessoas)
    if(elevador_quebrou == 'S'):
        a = elevador_quebrou
    qtde_pessoas = controle


print(a)