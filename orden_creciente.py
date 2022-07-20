
uno = int(input("Ingresa tu primer numero entero: "))
dos = int(input("Ingresa tu segundo numero entero: "))
tres = int(input("Ingresa tu tercer numero entero: "))

matriz = [uno, dos, tres]
matriz.sort()
menor = min(matriz)
mayor = max(matriz)


if uno != menor and uno != mayor :
    print('Orden creciente: ',menor," ",uno," ",mayor)

if dos != menor and dos != mayor :
    print('Orden creciente: ',menor," ",dos," ",mayor)

if tres != menor and tres != mayor :
    print('Orden creciente: ',menor," ",tres," ",mayor)

if uno == dos or uno == tres or dos == tres :
    print('Orden creciente: ',matriz[0]," ",matriz[1]," ",matriz[2],"NOTA, DOS O MAS DATOS SON IGUALES")
