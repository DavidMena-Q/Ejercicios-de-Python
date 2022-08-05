producto = input('¿Qué producto vendes?\n')

nombre = input('¿Cómo te llamas?\n')

anio = int(input('¿Año de creación?\n'))

anio = (anio - 2022) * (-1)

print(f'Tu producto se llamará:\n\"{producto} {nombre}\" y tiene {anio} años de antiguedad\nFelicitaciones!!')
# print('Tu producto se llamará:\n\"{} {}\" y tiene {} años de antiguedad\nFelicitaciones!!'.format(producto, nombre, anio))
