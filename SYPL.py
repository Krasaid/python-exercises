print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Bienvenido al Sistema de Pagos Laborales")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
while True:
    print("Menú Principal:")
    print("1. Calcular Salario")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input('Nombre del empleado: ')
        salario_base = float(input('Salario Base: '))
        desea_horas_extras = input('¿Desea ingresar horas extras? (si/no): ').strip().lower()
        if desea_horas_extras == 'si':
            print("Tipos de Horas Extras:")
            print("1. Diurnas")
            print("2. Nocturnas")
            print("3. Día de Descanso")
            print("4. Asueto")
                
            tipo_principal = int(input('Seleccione el tipo de horas extras: ').strip())
            if tipo_principal == 1:                    
                tipo_horas_extras = 1        
            elif tipo_principal == 2:
                tipo_horas_extras = 2                
            elif tipo_principal == 3:
                print("1. Diurnas\n2. Nocturnas")
                tipo_secundario = int(input('Seleccione el tipo específico de horas extras en Día de Descanso: ').strip())
                if tipo_secundario == 1:
                    tipo_horas_extras = 3
                elif tipo_secundario == 2:
                    tipo_horas_extras = 4
                else:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Opción no válida.  Por favor, seleccione una opción del menú.")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            elif tipo_principal == 4:        
                print("1. Diurnas\n2. Nocturnas")
                tipo_secundario = int(input('Seleccione el tipo específico de horas extras en Asueto: ').strip())
                if tipo_secundario == 1:
                    tipo_horas_extras = 5
                elif tipo_secundario == 2:
                    tipo_horas_extras = 6
                else:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Opción no válida.  Por favor, seleccione una opción del menú.")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")                
            horas_extras = float(input('Horas Extras: ').strip())
        else:
            tipo_horas_extras = 7
            horas_extras = 0

        bonificaciones = float(input('Bonificaciones: '))
        comisiones = float(input('Comisiones: '))
    
    elif opcion == "2":
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Gracias por usar el sistema de nóminas. ¡Hasta luego!")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        break
    else:
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Opción no válida. Por favor, seleccione una opción del menú.")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")