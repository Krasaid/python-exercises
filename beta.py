import sqlite3
print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Bienvenido al Sistema de Pagos Laborales")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------")

def menu_principal():
    print("Menú Principal:")
    print("1. Calcular Salario")
    print("2. Salir")


def calcular_tarifa_por_hora(salario_base):
    return salario_base / 22 / 8

def salrio_horas_extras(tarifa_hora, tipo_horas_extras, horas_extras):
    if tipo_horas_extras == 1:
        return tarifa_hora * horas_extras * 2  # 100%
    elif tipo_horas_extras == 2:
        return tarifa_hora * horas_extras * 2.5  # 150%
    elif tipo_horas_extras == 3:
        return tarifa_hora * horas_extras * 4  # 300%
    elif tipo_horas_extras == 4:
        return tarifa_hora * horas_extras * 4.75  # 375%
    elif tipo_horas_extras == 5:
        return tarifa_hora * horas_extras * 5  # 400%
    elif tipo_horas_extras == 6:
        return tarifa_hora * horas_extras * 6  # 500%
    else:
        return 0


def calcular_salario_bruto(salario_base, monto_horas_extras, bonificaciones, comisiones):
    return salario_base + monto_horas_extras + bonificaciones + comisiones


def calcular_deducciones(salario_bruto):
    isss = salario_bruto * 0.03
    afp = salario_bruto * 0.0725
    if salario_bruto <= 487.60:
        renta = 0
    elif salario_bruto <= 642.85:
        renta = 17.48 + 0.1 * (salario_bruto - 487.60)
    elif salario_bruto <= 915.81:
        renta = 32.70 + 0.2 * (salario_bruto - 642.85)
    else:
        renta = 60.00 + 0.3 * (salario_bruto - 915.81)
    deducciones_totales = isss + afp + renta
    return isss, afp, renta, deducciones_totales


def calcular_salario_neto(salario_bruto, deducciones_totales):
    return salario_bruto - deducciones_totales


def generar_recibo_txt(
    nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto
):
    archivo_txt = f"{nombre}_recibo.txt"
    with open(archivo_txt, "w") as file:
        file.write(f"Recibo de Pago para: {nombre}\n")
        file.write(f"Salario Bruto: ${salario_bruto:.2f}\n")
        file.write(f"ISSS: ${isss:.2f}\n")
        file.write(f"AFP: ${afp:.2f}\n")
        file.write(f"Renta: ${renta:.2f}\n")
        file.write(f"Deducciones Totales: ${deducciones_totales:.2f}\n")
        file.write(f"Salario Neto: ${salario_neto:.2f}\n")
    print(f"Recibo generado: {archivo_txt}")


def calcular_salario():
    nombre = input("Nombre del empleado: ")
    salario_base = float(input("Salario Base: ").strip())

    desea_horas_extras = input("¿Desea ingresar horas extras? (si/no): ").strip().lower()
    if desea_horas_extras == "si":
        print("Tipos de Horas Extras:")
        print("1. Diurnas")
        print("2. Nocturnas")
        print("3. Día de Descanso")
        print("4. Asueto")

        tipo_principal = int(input("Seleccione el tipo de horas extras: ").strip())
        if tipo_principal == 1:
            tipo_horas_extras = 1
        elif tipo_principal == 2:
            tipo_horas_extras = 2
        elif tipo_principal == 3:
            print("1. Diurnas\n2. Nocturnas")
            tipo_secundario = int(input("Seleccione el tipo específico de horas extras en Día de Descanso: ").strip())
            if tipo_secundario == 1:
                tipo_horas_extras = 3
            elif tipo_secundario == 2:
                tipo_horas_extras = 4
            else:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                return
        elif tipo_principal == 4:
            print("1. Diurnas\n2. Nocturnas")
            tipo_secundario = int(
                input(
                    "Seleccione el tipo específico de horas extras en Asueto: "
                ).strip()
            )
            if tipo_secundario == 1:
                tipo_horas_extras = 5
            elif tipo_secundario == 2:
                tipo_horas_extras = 6
            else:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                return
        else:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            return
        horas_extras = float(input("Horas Extras: ").strip())
    else:
        tipo_horas_extras = 7
        horas_extras = 0

    bonificaciones = float(input("Bonificaciones: ").strip())
    comisiones = float(input("Comisiones: ").strip())

    tarifa_hora = calcular_tarifa_por_hora(salario_base)
    monto_horas_extras = calcular_monto_horas_extras(tarifa_hora, tipo_horas_extras, horas_extras)
    salario_bruto = calcular_salario_bruto(salario_base, monto_horas_extras, bonificaciones, comisiones)

    isss, afp, renta, deducciones_totales = calcular_deducciones(salario_bruto)
    salario_neto = calcular_salario_neto(salario_bruto, deducciones_totales)

    print(f"\nEl salario bruto es: ${salario_bruto:.2f}")
    print(f"El salario neto es: ${salario_neto:.2f}")

    generar_recibo_txt(nombre, salario_bruto, isss, afp, renta, deducciones_totales, salario_neto)


while True:
    menu_principal()
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        calcular_salario()
    elif opcion == "2":
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Gracias por usar el sistema de nóminas. ¡Hasta luego!")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        break
    else:
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Opción no válida. Por favor, seleccione una opción del menú.")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
