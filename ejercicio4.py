
lista_alumnos = []

n = int(input("Ingrese la cantidad de alumnos: "))


for i in range(n):
    alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas=[]
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    datos_alumno = {
        "Alumno": alumno,
        "Notas": notas
    }
    
   
    lista_alumnos.append(datos_alumno)

print("\nListado de alumnos:")
for alumno in lista_alumnos:
    print(f"Alumno: {alumno['Alumno']}")
    print(f"Notas: {alumno['Notas']}\n")