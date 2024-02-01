#Crear un programa que permita ingresar los nombres de N alumnos
N = int(input("Ingresar cantidad de estudiantes: "))
i = 1
while N >= i:
    nombre = input("Nombre {}: ".format(i)) #.format se utiliza para dar un valor que es el va a ir dentro de {}
    i += 1 #Seria lo mismo que utilizar i = i + 1