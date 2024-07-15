import random
import csv
from statistics import geometric_mean


trabajadores = [
    {"nombre": "Juan Pérez", "sueldo": 0},
    {"nombre": "María García", "sueldo": 0},
    {"nombre": "Carlos López", "sueldo": 0},
    {"nombre": "Ana Martínez", "sueldo": 0},
    {"nombre": "Pedro Rodríguez", "sueldo": 0},
    {"nombre": "Laura Hernández", "sueldo": 0},
    {"nombre": "Miguel Sánchez", "sueldo": 0},
    {"nombre": "Isabel Gómez", "sueldo": 0},
    {"nombre": "Francisco Díaz", "sueldo": 0},
    {"nombre": "Elena Fernández", "sueldo": 0},
]

sueldos = []

def asignar_sueldos():
    for trabajador in trabajadores:
        trabajador["sueldo"] = random.randint(300000, 2500000)
    
    print("")
    print("Sueldos asignados")     


def clasificar():
    menores = [t for t in trabajadores if t["sueldo"]< 800000]
    entre = [t for t in trabajadores if 800000 <= t["sueldo"] <= 2000000]
    superiores = [t for t in trabajadores if t["sueldo"]> 2000000]

    print(" ")
    print("Sueldos menores a $800.000\nTOTAL:", len(menores))
    for t in menores:
        print(f"{t['nombre']}\t${t['sueldo']}")

    print("Sueldos entre a $800.000 y $2.000.000\nTOTAL:", len(entre))
    for t in entre:
        print(f"{t['nombre']}\t${t['sueldo']}")
    
    print("Sueldos mayores a $2.000.000\nTOTAL:", len(superiores))
    for t in superiores:
        print(f"{t['nombre']}\t${t['sueldo']}")
    
    total_sueldos = sum(t["sueldo"] for t in trabajadores)
    print("\nTOTAL SUELDOS: $", total_sueldos)

def estadisticas():
    
    sueldos = [t["sueldo"] for t in trabajadores]
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    media_geometrica = geometric_mean(sueldos)

    print(" ")
    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${promedio: .2f} ")
    print(f"Media geométrica: $ {media_geometrica: .2f}")

def reporte_sueldos():
    print("No pude profe perdon y no queria error synx o_o ")
def mostrar_menu():
    while True:
        print("\nMenu:")
        print("1) Asignar sueldos")
        print("2) Clasificar sueldos")
        print("3) Ver estadísticas")
        print("4) Reporte de sueldos")
        print("5) Salir del programa")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar()
        elif opcion == '3':
            estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            print("Finalizando el programa...")
            print("Desarrollado por Enzo Martínez")
            print("Rut 21.562.913-9")
            break
        else:
            print("Opción no válida, por favor elija una opción válida")
            
mostrar_menu()
    


    
