def transFormartexto(texto):
    listaLetras=list(texto.upper())
    vocales = 'AEIOU'
    nuevaLista=[]
    for letra in listaLetras:
        if letra not in vocales:
            nuevaLista.append(letra)
    return nuevaLista



texto = input('Ingrese texto a transformar:')

print(transFormartexto(texto))

