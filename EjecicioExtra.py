numeros_tarjetas = [
    "378282246310005",
    "371449635398431",
    "5555555555554444",
    "5105105105105100",
    "4111111111111111",
    "4012888888881881",
    "1234567890"
]

def algoritmo_luhn(numero_tarjeta):
    digits = [int(digit) for digit in str(numero_tarjeta)]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    suma_total = sum(digits)
    return suma_total % 10 == 0

def identificar_tipo_tarjeta(numero_tarjeta):
    if numero_tarjeta.startswith('34') or numero_tarjeta.startswith('37'):
        return 'AMEX'
    elif numero_tarjeta.startswith(('51', '52', '53', '54', '55')):
        return 'MASTERCARD'
    elif numero_tarjeta.startswith('4'):
        return 'VISA'
    else:
        return 'INVALID'

for numero_tarjeta in numeros_tarjetas:
    validacion = algoritmo_luhn(numero_tarjeta)
    tipo = identificar_tipo_tarjeta(numero_tarjeta)
    if validacion:
        print(f'Número de tarjeta: {numero_tarjeta}')
        print(f'La tarjeta es válida: {tipo}')
    else:
        print(f'Número de tarjeta: {numero_tarjeta}')
        print(tipo)
