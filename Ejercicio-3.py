#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
#y la media de todos los números introducidos.
#Para este problema se requiere de un acumulador y un contador
#Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
#por cada iteración el contador va incrementando en 1
#Ejemplo:
#contador = 0
#for i in range(5):
#   contador = contador + 1
#print(contador)
#Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada iteración,
#por cada iteración al valor inicial se le suman nuevos valores al acumulador
#Ejemplo:
#acumulador = 0;
#for i in range(5):
#    acumulador = acumulador + i
#print(acumulador)


acumulador =0
contador =0


while True:
    num = int(input(f"Digite un numero (Digite 0 para terminar): "))

    if num == 0:
        break

    acumulador += num
    contador += 1

if contador > 0:
    media = acumulador/contador
    print(f"La media de los numeros ingresados es {media}")
    print(f"La suma de los numeros ingresados es {acumulador}")
else:
    print("Introduce un numero")        