#En una tienda en línea, los datos de clientes están guardados en disco. 
#Se busca por número de cédula.

import random

cedulas = []

for i in range(1000):
    cedulas.append(random.randint(10000000000, 99999999999))

cedulaBuscada = int(input("Ingrese la cédula a buscar: "))

encontrado = False
for c in cedulas:
    if c == cedulaBuscada:
        encontrado = True
        break

if encontrado:
    print("Cliente encontrado.")
else:
    print("Cliente NO encontrado.")