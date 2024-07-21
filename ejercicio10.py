def validar_fecha():
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    while True:
        fecha = input('Ingrese la fecha (MM/DD/AAAA o "Mes DD, AAAA"): ')
        if ',' in fecha:
            partes = fecha.split()
            mes = partes[0]
            if mes not in meses:
                print('La fecha ingresada no es válida')
                continue
            else:
                # Verifica que el día y el año sean números válidos
                try:
                    dia = int(partes[1].strip(','))
                    anio = int(partes[2])
                    if dia < 1 or dia > 31:
                        print('El día debe estar entre 1 y 31')
                        continue
                except ValueError:
                    print('El día o el año no son válidos')
                    continue
                break
        else:
            partes = fecha.split('/')
            try:
                mes = int(partes[0])
                dia = int(partes[1])
                anio = int(partes[2])
                if mes < 1 or mes > 12:
                    print('El mes debe estar entre 1 y 12')
                    continue
                if dia < 1 or dia > 31:
                    print('El día debe estar entre 1 y 31')
                    continue
            except ValueError:
                print('La fecha ingresada no es válida')
                continue
            break
    return fecha  # ¡Debería ser fecha_convertida!

def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    if ',' in fecha:
        partes = fecha.split()
        mes = partes[0]
        dia = int(partes[1].strip(','))
        anio = int(partes[2])
        mes_numero = meses.index(mes) + 1
    else:
        partes = fecha.split('/')
        mes = int(partes[0])
        dia = int(partes[1])
        anio = int(partes[2])
        mes_numero = mes

    # Formatear la fecha como "AAAA-MM-DD"
    fecha_formateada = f"{anio:04}-{mes_numero:02}-{dia:02}"
    
    return fecha_formateada

# Validar y convertir la fecha
fecha_valida = validar_fecha()
fecha_convertida = convertir_fecha(fecha_valida)

print("Fecha en formato AAAA-MM-DD:", fecha_convertida)
