#Una aplicación ofrece descuentos con códigos numéricos ordenados. 
#Solo se aplican si el código es válido. 

codigosDescuento = [1001, 1005, 1010, 1020, 1050]
codigo = int(input("Ingrese el codigo: "))

inicio = 0
fin = len(codigosDescuento) - 1

while inicio <= fin:
    medio = (inicio + fin) // 2

    if codigosDescuento[medio] == codigo:
        print("Codigo valido. Descuento aplicado.")
        break
    elif codigosDescuento[medio] < codigo:
        inicio = medio + 1
    else:
        fin = medio - 1
else:
    print("Codigo invalido.")