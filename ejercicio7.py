def es_numero_perfecto(n):
    suma_divisores = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

def encontrar_numeros_perfectos(limite):
    numeros_perfectos = []
    for num in range(1, limite):
        if es_numero_perfecto(num):
            numeros_perfectos.append(num)
    return numeros_perfectos


print(f"Números perfectos menores que 1000:{encontrar_numeros_perfectos(1000)}",)