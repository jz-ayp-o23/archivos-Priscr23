"Priscila Cervantes"
"750722"
"Se toma la información que se encuentra en el archivo que se utilizará, se separan los elementos para darles a cada uno formato, junto con el promedio"
def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return round(promedio, 1)
with open('data/calificaciones.txt', 'r') as archivo_entrada, open('data/promedios.txt', 'w') as archivo_salida:
    lineas = archivo_entrada.readlines()
    for linea in lineas:
        palabras = linea.strip().split()
        nombre = palabras[0]
        apellido = palabras[1]
        calificaciones = [float(calificacion) for calificacion in palabras[2:]]
        promedio = calcular_promedio(calificaciones)
        linea_salida = f"{apellido.upper()}, {nombre}: {promedio}\n"
        archivo_salida.write(linea_salida)
