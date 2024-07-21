# Lista para almacenar los números que cumplen con las condiciones
numeros_validos = []

# Iterar a través del rango de 1500 a 2700
for num in range(1500, 2701):
    # Verificar si el número es divisible por 7 y múltiplo de 5
    if num % 7 == 0 and num % 5 == 0:
        # Si cumple, agregar a la lista
        numeros_validos.append(num)

# Imprimir los números que cumplen con las condiciones
print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(numeros_validos)