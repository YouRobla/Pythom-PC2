
listaNumeros = []
contadorPares = 0
contadorImpares = 0

while True:
    respuesta = input('¿Desea ingresar un número? (SI/NO): ')
    
    if respuesta.upper() == 'SI':
        num = int(input('Ingrese el número: '))
        listaNumeros.append(num)
        
        if num % 2 == 0:
            contadorPares += 1
        else:
            contadorImpares += 1
    elif respuesta.upper() == 'NO':
        print(f'Números ingresados: {listaNumeros}')
        print(f'Cantidad de números pares: {contadorPares}')
        print(f'Cantidad de números impares: {contadorImpares}')
        break
    else:
        print('Ingrese una respuesta válida (SI/NO).')
