def calcular_fatorial(num):
    if num == 0:
        return 1
    else:
        return num * calcular_fatorial(num - 1)

def calcular_S(N, P):
    if N < P:
        return "N deve ser maior ou igual a P"
    
    S = calcular_fatorial(N) / (calcular_fatorial(P) * calcular_fatorial(N - P))
    return S

N = int(input("Digite o valor de N: "))
P = int(input("Digite o valor de P: "))

resultado = calcular_S(N, P)
print("O valor de S é:", resultado)
