#Tienes un arreglo con los nombres de los estudiantes inscritos. 
#Un asistente desea saber si un estudiante llegó o no.

nombres = ["Ana", "Luis", "Carlos", "María", "Pedro"]

nombreBuscado = input("Ingrese el nombre del estudiante: ")

encontrado = False

for nombre in nombres:
    if nombre == nombreBuscado:
        encontrado = True
        break

if encontrado:
    print("El estudiante SI asistio")
else:
    print("El estudiante NO asistio")