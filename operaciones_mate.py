x = int(input('Ingresa el valor de la variable independiente: '))
y = 4 + x
z = x + y - 1

print(f'''{x} más {y} = {x + y}
{x} menos {y} = {x - y}
{x} por {y} = {x * y}
{y} divido {x} = {y / x}
{z} divido al piso de {x} = {z // x}
{z} módulo de  {x} = {z % x}
{x} elevado a la potencia de {y} = {x** y}
La raíz cuadrada de {y} = {y**(1/2)}
La raíz cuadrada redondeada de {y} = {round(y**(1/2), 3)}
''')
