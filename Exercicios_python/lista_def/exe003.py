'''0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Above 2000.00'''


def aumento(salario):
    new_salario = salario
    porcentual = ''
    if(salario <= 400):
        salario = salario * 0.15
        porcentual = '15 %'
    elif(salario > 400 and salario <= 800):
        salario = salario * 0.12
        porcentual = '12 %'
    elif(salario > 800 and salario <= 1200):
        salario = salario * 0.10
        porcentual = '10 %'
    elif(salario > 1200 and salario <= 2000):
        salario = salario * 0.07
        porcentual = '7 %'
    else:
        salario = salario * 0.04
        porcentual = '4 %'
    print(f"Novo salario: {new_salario+salario:.2f}")
    print(f"Reajuste ganho: {salario:.2f}")
    print(f"Em percentual: {porcentual}")


salario = float(input(""))
aumento(salario)








