from datetime import date
#Quiere usar una fecha con algo, normalmente una cadena. 
#Si, por ejemplo, desea mostrar la fecha de hoy en la consola, podría experimentar algún problema:
#print("Today's date is: " + date.today()) # (este codigo dara error)
#Para que este código funcione, debe convertir la fecha en una cadena. 
#Para realizar esta conversión, use la función de utilidad str():
print("Today's date is: " + str(date.today()))