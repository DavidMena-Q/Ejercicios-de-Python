string = 'Este es un string'

# index sirve para encontrar la posición de un elemento un elemento de un string
# extraer caracter [2:3:4]
# join convertir lista en string
lista_de_string = string.split(' ')
unir_lista = ' '.join(lista_de_string)

print(f'''{string}
posición:{string.index("r")}
elemento:{string[5]}
Sub_str: {string[10:1:-1]}
operación con str: {string[0:4] * 4}
Mayúsculas: {string.upper()}
Minusculas: {string.lower()}
Lista: {lista_de_string}
Unir lista: {unir_lista}
reverso: {lista_de_string.reverse()}
Rempalazar texto: {string.replace('un', 'otro')}
la palabra Este esta en string?: {'Este' in string}
la palabra Pablo esta en string?: {'Pablo' in string}
la palabra Este no esta en string?: {'Este' not in string}
la palabra Pablo no esta en string?: {'Pablo' not in string}''')

