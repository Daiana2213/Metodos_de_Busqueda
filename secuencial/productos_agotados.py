#Una tienda tiene una lista de productos agotados. 
#Se desea saber si un producto aún no está disponible. 

agotados = ["arroz", "leche", "huevos", "azúcar"]
producto = input("Ingrese el producto a buscar: ")
posicion = -1

for i in range(len(agotados)):
    if agotados[i] == producto:
        posicion = i
        break

if posicion != -1:
    print(f"El producto SI esta agotado en la posición {posicion}.")
else:
    print("El producto NO esta agotado.")