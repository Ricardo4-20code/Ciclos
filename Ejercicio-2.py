#'''
#Crea un programa que permita adivinar un número. La aplicación genera un 
#número aleatorio del 1 al 100. A continuación va pidiendo números y va 
#respondiendo si el número a adivinar es mayor o menor que el introducido,
#a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
#El programa termina cuando se acierta el número (además te dice en cuantos 
#intentos lo has acertado), si se llega al limite de intentos te muestra el 
#número que había generado.
#Para genear un número entero aleatorio se utiliza la función randint
#del paquete random

#import random
#aleatorio = random.randint(limite_inf, limite_sup)
#'''
import random
num_secret= random.randint(1,100)
intentos_restantes=10
intentos_realizados=0

print("Tienes que adivinar un numero del 1 al 100")
print("Solo tienes 10 intentos")

while intentos_restantes >0: 
    intento=int(input(f"Ingresa un numero: "))
    intentos_realizados +=1
    intentos_restantes -=1

    if num_secret == 0: 
        print(f"FELICIDADES, HAS ADIVINADO EL NUMERO SECRETO EN {intentos_realizados} INTENTOS")
        break
    elif num_secret > intento:
        print(f"El numero a adivinar es mayor a {intento}")
    else:
        print(f"El numero a adivinar es menor a {intento}")

    