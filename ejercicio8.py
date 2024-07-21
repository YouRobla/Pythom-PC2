def calcular_factorial(num):
    if num < 0:
        raise ValueError("El número debe ser un entero no negativo")
    factorial = 1
    for i in range(2, num + 1):  
        factorial *= i
    return factorial

print(calcular_factorial(10))  
    