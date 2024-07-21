def serieFibonacci(limite):
    serie = []
    a, b = 0, 1
    while a <=limite:
        serie.append(a)
        a,b=b,a+b
    return serie

print(serieFibonacci(50))