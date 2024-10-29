import string
from itertools import combinations_with_replacement
from random import random,choice

def gerar_senha(valores,tamanho):
    comb = combinations_with_replacement(valores, tamanho)

    print(list(comb))

valores = 'abc'
gerar_senha(valores, 5)