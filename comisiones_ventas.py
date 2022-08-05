nombre = input('Ingrese su nombre: ')

volumen_ventas = float(input('Ingrese su volumen total de ventas: '))

volumen_ventas = round(volumen_ventas, 2)

comision_13 = round((volumen_ventas * 13)/100, 2)

print(f'{nombre} has ganado ${comision_13} de comisión '
      f'por tu volumen de ventas de ${volumen_ventas} \nFelicitaciones!!')
