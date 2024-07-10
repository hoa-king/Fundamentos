import random
import csv

# Lista de estudiantes
alumnos = ["Juan Pérez", "María García", "Carlos López", 
           "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
           "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Diccionario para almacenar créditos
creditos_estudiantes = {}

# Funciones para la gestión de créditos

def simular_asignacion_creditos():
    global creditos_estudiantes  # Acceso al diccionario global
    for alumno in alumnos:
        credito_aleatorio = random.randint(50, 200)
        creditos_estudiantes[alumno] = credito_aleatorio
    print(creditos_estudiantes)
    return creditos_estudiantes

def clasificar_creditos(creditos_estudiantes):
    rangos = {
        "Bajo": 0,
        "Medio": 0,
        "Alto": 0
    }
    for credito in creditos_estudiantes.values():
        if credito < 100:
            rangos["Bajo"] += 1
        elif credito <= 150:
            rangos["Medio"] += 1
        else:
            rangos["Alto"] += 1
    return rangos

def calcular_estadisticas_creditos(creditos_estudiantes):
    valores_creditos = list(creditos_estudiantes.values())
    maximo_credito = max(valores_creditos)
    minimo_credito = min(valores_creditos)
    promedio_credito = sum(valores_creditos) / len(valores_creditos)
    return {
        "Máximo": maximo_credito,
        "Mínimo": minimo_credito,
        "Promedio": promedio_credito
    }

def generar_reporte_csv(creditos_estudiantes, rangos, estadisticas):
    with open("reporte_creditos.csv", "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)

        # Encabezado del reporte
        escritor_csv.writerow(["Nombre", "Crédito", "Rango"])

        # Listado de estudiantes con créditos y rangos
        for alumno, credito in creditos_estudiantes.items():
            rango = "Bajo" if credito < 100 else "Medio" if credito <= 150 else "Alto"
            escritor_csv.writerow([alumno, credito, rango])

        # Línea en blanco para separar secciones
        escritor_csv.writerow([])

        # Encabezado de las estadísticas
        escritor_csv.writerow(["Estadísticas"])

        # Listado de las estadísticas calculadas
        for estadistica, valor in estadisticas.items():
            escritor_csv.writerow([estadistica, valor])

def menu_principal():
    while True:
        print("\nSistema de Gestión de Créditos")
        print("----------------------------")
        print("1. Simular asignación de créditos")
        print("2. Clasificar créditos")
        print("3. Calcular estadísticas de créditos")
        print("4. Generar reporte CSV")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            creditos_estudiantes = simular_asignacion_creditos()
            print("Créditos asignados exitosamente.")
        elif opcion == "2":
            rangos = clasificar_creditos(creditos_estudiantes)
            print("Clasificación de créditos:")
            for rango, cantidad in rangos.items():
                print(f"{rango}: {cantidad} estudiantes")
        elif opcion == "3":
            estadisticas = calcular_estadisticas_creditos(creditos_estudiantes)
            print("Estadísticas de créditos:")
            for estadistica, valor in estadisticas.items():
                print(f"{estadistica}: {valor}")
        elif opcion == "4":
            if creditos_estudiantes:
                rangos = clasificar_creditos(creditos_estudiantes)
                estadisticas = calcular_estadisticas_creditos(creditos_estudiantes)
                generar_reporte_csv(creditos_estudiantes, rangos, estadisticas)
                print("Reporte CSV generado exitosamente.")
            else:
                print("No se han asignado créditos a los estudiantes. Ejecute la opción 1 primero.")
        elif opcion == "5":
            print("Saliendo del programa")

menu_principal()
