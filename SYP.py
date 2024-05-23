# calcalar el salario bruto = csbr
# calcular el salario neto  = csnt
# salario base              = sb
# horas extras              = hx
# tipo de horas extras      = thex
# bonificaciones            = bonif
# comisiones                = comics
# tarifa por hora           = th
# salario por hora extras   = shex
# salario bruto             = sbr
# isss                      = isss
# afp                       = afp
# salario neto              = snt


# Definir funciones
def csbr(sb, thex, bonif, comics):
    # tarifa por hora
    th = sb / 22 / 8
    shex = 0
    if thex == 1:
        shex = th * hx * 2       # 100%
    elif thex == 2:
        shex = th * hx * 2.5     # 150%
    elif thex == 3:
        shex = th * hx * 4       # 300%
    elif thex == 4:
        shex = th * hx * 4.75    # 375%
    elif thex == 5:
        shex = th * hx * 5       # 400%
    elif thex == 6:
        shex = th * hx * 6       # 500%
    elif thex == 7:
        print("No hay horas extras")
    else:
        print("Opción no válida")
    sbr = sb + shex + bonif + comics
    return sbr

def csnt(sbr):
    isss = sbr * 0.03
    afp = sbr * 0.0725
    snt = sbr - (isss + afp)
    return snt

# Solicitar entradas del usuario
sb = float(input('Salario Base: '))
print("Horas Extras: \n1. Horas extras Diurnas \n2. Horas extras Nocturnas \n3. Horas extras en Descanso Diurno  \n4. Horas extras en Descanso Nocturno \n5. Horas extras en Asueto Diurno \n6. Horas extras en Asueto Nocturno \n7. No hay horas extras")
thex = int(input('Tipo de Horas Extras: '))
hx = float(input('Horas Extras: '))
bonif = float(input('Bonificaciones: '))
comics = float(input('Comisiones: '))

# Calcular salarios
sbr = csbr(sb, thex, bonif, comics)
snt = csnt(sbr)

# Imprimir resultados
print(f"El salario bruto es: {sbr:.2f}")
print(f"El salario neto es: {snt:.2f}")
