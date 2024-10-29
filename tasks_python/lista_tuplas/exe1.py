def lista_para_decimal(bits):
    bits_str = ''.join(map(str, bits))
    decimal = int(bits_str, 2)
    return decimal

def inteiro_para_lista_bits(numero):
    binario_str = bin(numero)[2:]
    bits = [int(bit) for bit in binario_str]
    return bits


bits = [1, 0, 1, 0]
resultado = lista_para_decimal(bits)
print(f"O número decimal é: {resultado}")


numero = int(input("Numero para binario: "))
bits = inteiro_para_lista_bits(numero)
print(f"A lista de bits é: {bits}")





















'''
def complemento2_para_decimal(bits):
    n = len(bits)
    if bits[0] == 0:
        return int(''.join(map(str, bits)), 2)
    else:
        inversao = ''.join('1' if bit == '0' else '0' for bit in ''.join(map(str, bits)))
        complemento2 = int(inversao, 2) + 1
        return -complemento2

bits = [1, 1, 0, 1]
resultado = complemento2_para_decimal(bits)
print(f"O número decimal é: {resultado}")
'''
