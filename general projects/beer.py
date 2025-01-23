nombre_y_apellido = input('Cual es tu nombre y apellido?')
ventas_mensuales = float(input('Cuanto vendiste este mes en $?'))
comision = '13%'
monto = round(ventas_mensuales * 0.13,2)

print(f'Hola {nombre_y_apellido}, como estas?\nComo este mes vendiste ${ventas_mensuales} y la comision es del {comision}...\n\
Este mes te corresponden: ${monto} FELICIDADES!!!')
