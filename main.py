#Para probar cada uno de ellos de forma sencilla ^^

print("Menu de busqueda, elige el que deseas:")
print("1. Asistencia")
print("2. Productos agotados")
print("3. Buscar nota")
print("4. Codigo descuento")
print("5. Clientes")

opcion = input("Selecciona una de estas: ")

if opcion == "1":
    import secuencial.asistencia
elif opcion == "2":
    import secuencial.productos_agotados
elif opcion == "3":
    import binaria.buscar_nota
elif opcion == "4":
    import binaria.codigos_descuento
elif opcion == "5":
    import externa.clientes