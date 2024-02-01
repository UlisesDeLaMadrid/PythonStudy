# Caso 3 - Bucle infinito con condicional
iterator = 0
while iterator != 10: # 10 != 10 Falso
    print(iterator)
    iterator = iterator + 1 #Si se cambia el valor por -1 el bucle vuelve a ser infinito.
