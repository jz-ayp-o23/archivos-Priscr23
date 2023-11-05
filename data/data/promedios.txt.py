# Abrir el archivo de entrada en modo lectura
with open('data/calificaciones.txt', 'r') as entrada:
    # Crear un diccionario para almacenar los promedios de calificaciones
    promedios = {}
    
    # Leer cada línea del archivo de entrada
    for linea in entrada:
        # Dividir la línea en palabras (nombre, apellido y calificaciones)
        partes = linea.split()
        
        # Extraer el nombre y el apellido
        nombre = partes[0]
        apellido = partes[1]
        
        # Extraer las calificaciones y convertirlas a números
        calificaciones = [float(x) for x in partes[2:]]
        
        # Calcular el promedio de calificaciones
        promedio = sum(calificaciones) / len(calificaciones)
        
        # Almacenar el promedio en el diccionario usando el apellido como clave
        promedios[apellido.upper()] = (nombre, promedio)

# Abrir el archivo de salida en modo escritura
with open('data/promedios.txt', 'w') as salida:
    # Escribir los promedios en el formato deseado
    for apellido, (nombre, promedio) in promedios.items():
        linea = f'{apellido}, {nombre}: {promedio:.1f}\n'
        salida.write(linea)

