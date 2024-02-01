N = int(input("Ingresar cantidad de alumnos: "))
for i in range(N):
    nombre = input("Alumno {}: ".format(i + 1))
    M = int(input("Ingresar cantidad de cursos: "))
    for j in range (M):
        curso_nombre = input ("Curso {}: ".format(j + 1))