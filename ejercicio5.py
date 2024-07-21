import math
def detectarNumPrimo(num):
    if num <=1:
        return False
    else:
        for i in range (2,int(math.sqrt(num)+1)):
            if num%i==0:
                return False
        return True
    
def sumaPrimos(limite):
    suma = 0
    for i in range(2,limite):
        if detectarNumPrimo(i):
            suma+=i
    return suma

def listaNumerosPrimos(limite):
    numPrimos=[]
    for i in range(2,limite):
        if detectarNumPrimo(i):
            numPrimos.append(i)
    return numPrimos
    
print(f'La lista de todos los números primos menores que 100: {listaNumerosPrimos(100)}')
print(f'La suma de todos los numeros primeros menores que 100: {sumaPrimos(100)} ')