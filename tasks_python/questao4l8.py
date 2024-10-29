def calculaFatorial(num):
    res = 1
    count = 1

    while count <= num:
        res *= count
        count += 1
    return res
    

var = calculaFatorial(0)
print(var)