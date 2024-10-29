def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {resultado}m².')

print('Controle de Terrenos')
print('-' * 20)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))

area(larg, comp)
