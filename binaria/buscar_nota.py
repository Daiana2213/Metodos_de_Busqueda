#Un profesor tiene las notas finales ordenadas 
#Y desea saber si un estudiante obtuvo una calificación específica. 

notas = [60, 70, 75, 80, 85, 90, 95]
notaBuscada = int(input("Ingrese la nota a buscar: "))

inicio = 0
fin = len(notas) - 1
encontrado = False

while inicio <= fin:
    medio = (inicio + fin) // 2

    if notas[medio] == notaBuscada:
        encontrado = True
        break
    elif notas[medio] < notaBuscada:
        inicio = medio + 1
    else:
        fin = medio - 1

if encontrado:
    print("La nota existe.")
else:
    print("La nota NO existe.")