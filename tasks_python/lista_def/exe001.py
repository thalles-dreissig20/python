import time

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = -passo
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            time.sleep(0.5)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ', flush=True)
            time.sleep(0.5)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
