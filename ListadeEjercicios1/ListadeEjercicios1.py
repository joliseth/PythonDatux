
print("LISTA DE EJERCICIOS 1\nAlumna: Joanna Lapa\n")

## PREGUNTA 1
## Realizar un programa que ingrese sus datos personales e imprimirlos

print("PREGUNTA 1\nPor favor, ingrese datos personales")
apellido_paterno=str(input("Apellido Paterno: "))
apellido_materno=str(input("Apellido Materno: "))
nombres=str(input("Nombres: "))
print(f"Sus datos ingresados son:\n{apellido_paterno.upper()} {apellido_materno.upper()} , {nombres.upper()}","\n")


## PREGUNTA 2
## Calcule el área de un círculo con radio ingresado desde el teclado

import math
radio=float(input("PREGUNTA 2\nIngrese radio del círculo: "))
if radio > 0:
    area_circulo=math.pi*(radio**2)
    print(f"Área del círculo es igual a: {area_circulo}","\n")
else:
    print("Ingrese un valor positivo","\n")


## PREGUNTA 3
## Ingrese 3 valores y realice las operaciones de suma ,resta y multiplicación

print("PREGUNTA 3\nPor favor, ingrese valores")
valor_1=float(input("Primer varlor: "))
valor_2=float(input("Segundo varlor: "))
valor_3=float(input("Tercer varlor: "))
suma=valor_1+valor_2+valor_3
resta=valor_1-valor_2-valor_3
multiplicacion=valor_1*valor_2*valor_3
print(f"Resultados:\n-Suma: {suma}\n-Resta: {resta}\n-Multiplicación: {multiplicacion}","\n")


## PREGUNTA 4
## Ingrese un valor e imprima el tipo de dato

print("PREGUNTA 4\nPor favor, ingrese el dato para mostra el tipo")
dato=str(input("Dato: "))
tipo=type(dato)
print(f"El tipo de dato es {tipo}")

dato=int(input("Dato: "))
tipo=type(dato)
print(f"El tipo de dato es {tipo}")

dato=float(input("Dato: "))
tipo=type(dato)
print(f"El tipo de dato es {tipo}","\n")

## * Considerando que el usuario digite cualquier dato:

import math
valor=input("*Ingresando cualquier valor*\nIngrese valor: ")
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
  
indice = 0
while indice < len(valor):
    letra = valor[indice]
    indice += 1    
if letra in abc:
    print(type(valor),"string\n")
elif float(valor)%2==0:
    print(type(int(valor)),"entero\n")
elif float(valor)%2!=0:
    if math.modf(float(valor))[0]!=0:
        print(type(float(valor)),"decimal\n")
    else: 
        print(type(int(valor)),"entero\n")


## PREGUNTA 5
## Realice un programa que imprima la ubicación de su carpeta donde se encuentra
## trabajando

import sys
variable =sys.argv[0]
print("PREGUNTA 5\n",f"La ruta de la carpeta es: {variable}\n")


## PREGUNTA 6
## Realice un programa que calcule la suma de los números hasta el valor ingresado
## Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5

print("PREGUNTA 6\nIngrese los valores (enteros, decimales, positivos o negativos) que desea sumar,\n"
      "para obtener la suma presione '0'\n")

lista=[]
m=float(input("Ingrese valor: "))

while m != 0:    
    lista.append(m)
    m=float(input("Ingrese valor: "))
    if m == 0:
        break;
print(f"La suma de los valores ingresados es: {sum(lista)}\n")

  
## PREGUNTA 7
## Realiza un programa que lea 2 números por teclado y determine los siguientes
## aspectos:

## a) Si los dos números son iguales
## b) Si los dos números son diferentes
## c) Si el primero es mayor que el segundo
## d) Si el segundo es mayor o igual que el primero

print("PREGUNTA 7\nIngrese dos nùmeros(enteros, decimales, positivos o negativos) utilizando el teclado\n")

num1=float(input("Ingrese número 1: "))
num2=float(input("Ingrese número 2: "))

if num1 != num2:
    if num1 > num2:
        print("Los números son diferentes y el primer número es mayor que el segundo\n")
    else:
        print("Los números son diferentes y el segundo número es mayor que el primero\n")
else:
    print("Los número son iguales\n")


## PREGUNTA 8
## Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
## pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
## usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña=str(input("PREGUNTA 8\nRegistre contraseña: "))
print("Contraseña guardada\n")

variable=str(input("Introduce contraseña para acceder: "))

if contraseña.lower() == variable.lower():
    print("Contraseña correcta\n")
else:
    print("Contraseña incorrecta\n")


## PREGUNTA 9
## Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
## impar

num=int(input("PREGUNTA 9\nIngrese número entero: "))

if num != 0:
    if num%2 == 0:
        print(f"El número {num} es par\n")
    else:
        print(f"El número {num} es impar\n")
else:
    print("Ingresar un valor diferente a 0\n")


## PREGUNTA 10 
## Realizar un programa que calcule la penalidad por la mora de una deuda,sabiendo que si se
## demora de 1 día a 10 se le agrega el 5% , si se demora hasta 30 días se le agrega 8% y pasando
## el rango máximo se le agrega un 10%

deuda=float(input("PREGUNTA 10\nIngrese deuda: "))
dias=int(input("Ingrese días de retrazo: "))
tasa=[0.05,0.08,0.10]

if dias>=1 and dias<11:
    print(f"Tasa de la mora por {dias} días = {tasa[0]}\n",
          f"Penalidad = {deuda*tasa[0]}\n",f"Total a pagar = {deuda*(1+tasa[0])}\n")
elif dias>=11 and dias<31:
    print(f"Tasa de la mora por {dias} días = {tasa[1]}\n",
          f"Penalidad = {deuda*tasa[1]}\n",f"Total a pagar = {deuda*(1+tasa[1])}\n")
else:
    print(f"Tasa de la mora por {dias} días = {tasa[-1]}\n",
          f"Penalidad = {deuda*tasa[-1]}\n",f"Total a pagar = {deuda*(1+tasa[-1])}\n")


## PREGUNTA 11.A
## Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un
## menú:
## a) Mostrar una suma de los dos números
## b) Mostrar una resta de los dos números (el primero menos el segundo)
## c) Mostrar una multiplicación de los dos números
## d) En caso de introducir una opción inválida, el programa informará de que no es correcta.

print("PREGUNTA 11.A\nElige la opción que desea ejecutar:\n" 
       "a) Suma\n"
       "b) Resta\n"
       "c) Multiplicación\n")

lista=['a','b','c']
opcion=str(input("Ingrese opción: "))

while opcion in lista:
    n1=float(input("Ingrese número 1: "))
    n2=float(input("Ingrese número 2: "))
    if opcion == 'a':
        print(f"Suma = {n1+n2}\n")
    elif opcion == 'b':
        print(f"Resta = {n1-n2}\n")
    else:
        print(f"Multiplicación = {n1*n2}\n")
    break;
else:
    print("Opción no válida\n")


## PREGUNTA 11.B
## Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es
## vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle
## que no se puede procesar el dato

letra=str(input("PREGUNTA 11.B\nIngrese letra: "))
vocal=["a","e","i","o","u"]

while len(letra) == 1:
    if letra in vocal:
        print(f"Es la vocal {letra}\n")
    else:
        print(f"Es la consonante {letra}\n")
    break;
else:
    print("No se puede procesar el dato\n")


## PREGUNTA 12
## Defina una lista de 5 estudiantes realice lo siguiente :
## -el tamaño de la lista
## -el ultimo elemento
## -Revierta los elementos

print("PREGUNTA12\nRegistre el nombre de 5 estudiantes")
lista_estudiantes=[]
nom_estudiante=str(input("Ingrese nombre de estudiante: "))

while len(lista_estudiantes) >= 0:
    lista_estudiantes.append(nom_estudiante)
    nom_estudiante=str(input("Ingrese nombre de estudiante: "))
    if len(lista_estudiantes) == 5:
       break;
print(F"- La lista de estudiantes es: {lista_estudiantes}")
print(f"- Tamaño de la lista es {len(lista_estudiantes)}")
print(f"- El último elemento de la lista es {lista_estudiantes[-1]}")
lista_estudiantes.reverse()
print(f"- Lista revertida: {lista_estudiantes}\n")


## PREGUNTA 13
## Defina un diccionario con una tupla y una lista de elementos, modifique el ultimo elemento

diccionario= {
    "tupla":("a","b","c"),
    "lista":[1,2,3]
}

print("PREGUNTA 13")
print(diccionario)
print(type(diccionario))
print(type(diccionario["tupla"]))
print(type(diccionario["lista"]))

llaves=diccionario.keys()
print(llaves)

valores=diccionario.items()
print(valores)

diccionario["lista"].clear()
print(diccionario["lista"])

diccionario["lista"].append(89)
print(diccionario["lista"])

diccionario["lista"].append([7,8,15,16])
print(diccionario["lista"])

print(diccionario)


## PREGUNTA 14
## Realice un Menú interactivo que tenga las opciones de saludar ,una operación matemática y
## salir

print("\nPREGUNTA 14\nElige la opción que desea ejecutar:\n" 
       "1) Saludo\n"
       "2) Multiplicación\n"
       "3) Salir de la sesión\n")

import math
opcion=int(input("Ingrese opción: "))
lista=[1,2,3]

while opcion in lista:
    if opcion == 1:
        print("Hola! que tengas un buen día\n")
        break;
    elif opcion == 2:
        print("Para obtener resultado ingrese '0' al final\n")
        num=[]
        n=float(input("Ingrese número: "))        
        while n != 0:
            num.append(n)
            n=float(input("Ingrese número: "))                    
            if n == 0:
              break;
        print(f"Multiplicación de lo números = {math.prod(num)}\n")
        break;
    else:
        print("Salió de la sesión\n")
        break;
else:
    print("Opción incorrecta\n")


## PREGUNTA 15
## Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de
## edad
## Nota: cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]

print("PREGUNTA 15\nIngrese los datos personales, para conculir con el registro digite '0' en ambos datos")
datos=str(input("Ingrese nombre y apellido: "))
edad=int(input("Ingrese edad: "))
listaA=[]   ## Lista con personas mayores de edad
listaB=[]   ## Lista con personas menores de edad

while datos != 0 and edad !=0:
    if edad >= 18:
        listaA.append([datos,edad])
        datos=str(input("Ingrese nombre y apellido: "))
        edad=int(input("Ingrese edad: "))
    elif edad < 18:
        listaB.append([datos,edad])
        datos=str(input("Ingrese nombre y apellido: "))
        edad=int(input("Ingrese edad: "))
    if datos == 0 and edad == 0:   
        break;
print("Lista: ",listaA)

print("\nFin de los ejercicios\n")










