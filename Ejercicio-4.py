#Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5

num = int (input(f"Digite el numero a multiplicar: "))

for i in range(1,6):
    print(f"Tabla del {num}")
    for i in range(1,11):
        print(f"{num} * {i} = {num*i} ")