
print("\nLISTA DE EJERCICIOS 2\nAlumna: Joanna Lapa\n")

## PREGUNTA 1
## Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el
## número

print("\nPREGUNTA 1\n")

lista=[]

def multiplo(a,b):
    if (a>=0 and b>=0):
        if a < b:
            for i in range(a,b+1):
                if i%2==0:
                    lista.append(i)                         
            print(lista,"\n")   ## imprime los valores multiplos de 2 en una lista de un rango ingresado 
            for j in lista:
                print(j,"\n")   ## imprime cada valor multiplo de 2 por separado de un rango ingresado                      
        else:
            print("Primer valor ingresado debe ser menor al segundo valor ingresado\n")
    else:
        print("Solo se aceptan valores positivos mayores a 0\n")

multiplo(4,10)
multiplo(10,4)
multiplo(-10,4)


## PREGUNTA 2
## Realizar un programa que dibuje un cuadrado en consola con * ,usando bucles

print("PREGUNTA 2\n")

## Alternativa 1

def cuadrado(a):
    for j in range(a):
        for i in range (a):
            print("*",end="")  ### imprime * generados i veces en una sola linea horizontal
        print("")  ### repite j veces en columna vertical el contenido anterior

cuadrado(4)
print("\n")
cuadrado(10)
print("\n")

## Alternativa 2

a=int(input("Ingrese lado del cuadrado: "))

for j in range(a):
    print("*"*a)

print("\n")


## PREGUNTA 3
## Realizar un programa que dibuje un triángulo en consola con * ,usando bucles

print("PREGUNTA 3\n")

def triangulo(a):
    for i in range(a):
        print(" "*(a-i-1)+"*"*(2*i+1))

triangulo(5)
print("\n")
triangulo(10)
print("\n")


## PREGUNTA 4
## Realizar un programa que inserte valores en una lista desde el 1 hasta el 100 saltando en
## 2 en 2 . Ejemplo : [ 1,3 ,5 ,...]

print("PREGUNTA 4\n")

lista=[]

def inserteValor(a,b):
    if len(lista) != 0:
        lista.clear()  
    for i in range(a,b+1):    
        lista.append(i)        
    print(lista[::2])

inserteValor(1,100)
inserteValor(2,10)
inserteValor(50,75)


## PREGUNTA 5
## Definir una función que multiplique 2 números mayores de cero.

print("\nPREGUNTA 5\n")

def multiplicación(x,y):
    if x>0 and y>0:
        print(f"La multiplicación de los números es: {x*y}")
    else:
        print("Ingrese valores mayores a 0")

multiplicación(4,5)
multiplicación(-4,5)


## PREGUNTA 6
## Definir las siguientes funciones :
## -saludar(nombre)
## -realizarTarea(tarea)
## -despedirse(nombre)
## *las funciones imprimen lo que se envía como parámetro

print("\nPREGUNTA 6\n")

def funciones(opcion:int,mensaje:str):   
    if opcion==1:
        print(f"Hola {mensaje}!")
    elif opcion==2:
        print(f"Realizar tarea de {mensaje}.")
    elif opcion==3:
        print(f"Bye bye {mensaje}.")
    else:
        print("Opción no validada, digite 1,2 o 3.")

funciones(1,"Nick")
funciones(2,"Matemática")
funciones(3,"Andrea")
funciones(4,"Limpieza")


## PREGUNTA 7
## Definir una función que retorne el mayor valor al ingresar 2 números

print("\nPREGUNTA 7\n")

def comparacion(a:int,b:int):
    if a>=0 and b>=0:
        if a>b:
            print(f"El mayor valor es {a}")
        elif b>a:
            print(f"El mayor valor es {b}")
        else:
            print(f"Ambos valores son iguales")
    else:
        print("Digite valores mayores a 0")

comparacion(5,6)
comparacion(10,7)
comparacion(4,4)
comparacion(-3,4)


## PREGUNTA 8
## Definir una función que imprima los argumentos ingresados desde linea de comandos
## Nota: Usar import sys.argv => *args

print("\nPREGUNTA 8\n")

import sys

def imprimir_ruta(*ruta):
    for rut in ruta:
        print(f"La ruta es {rut}\n")

imprimir_ruta(sys.argv)
imprimir_ruta("Vía Expresa")

def imprimir_argumentos(**argu):
    print(f"Argumento ingresado: {argu}\n")
    for arg in argu:
        print(arg,"=>",argu[arg],"\n")

imprimir_argumentos(Numero=456,Saludo="Hello my friend!",ListaPlanetas=["venus","marte","jupiter"])


## PREGUNTA 9
## Realizar una función que tenga por parámetro un lista de numeros y aumente cada
## elemento en +1

print("PREGUNTA 9\n")

listanum=[]

def numero(num):
    if len(listanum)!=0:
        listanum.clear()
    for i in range(num):
        i+=1
        listanum.append(i+1)
    print(listanum)

numero(3)
numero(10)
numero(7)
print("\n")

## Alternativa ingresando diferentes valores en la lista

lista=[]
num=int(input("Ingrese numero: ")) ## ingrese valor 0 para imprimir la lista

while num != 0:
    lista.append(num+1)
    num=int(input("Ingrese numero: "))
    if num==0:
        break
print(lista)
print("\n")


## PREGUNTA 10
## Realizar un programa que realice las siguientes funciones de string al texto.
## -split
## -count
## -find
## -uppercase
## -lowercase
## texto=”Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
## Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
## impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y
## los mezcló de tal manera que logró hacer un libro de textos especimen.”

print("\nPREGUNTA 10\n")

mi_texto="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."
    
print(mi_texto.split(sep=" "),"\n")

print(mi_texto.split(sep=" ", maxsplit=10),"\n")

print(mi_texto.count("texto"),"\n")

print(mi_texto.find("industrias"),"\n")

print(mi_texto.upper(),"\n")

print(mi_texto.lower(),"\n")


## PREGUNTA 11
## Definir los atributos y métodos de una de las siguientes clases.
## - Persona
## - Gato
## - Producto

print("PREGUNTA 11\n")

class microondas:
    def __init__(self):
        self.potencia=""
        self.capacidad=""
        self.material=""
        self.medidas=""
        self.peso=""
        self.color=""
        self.panel=""
    def calentar(self):
        self.panel=1 
    def cocinar(self):
        self.panel=2 
    def dorar(self):
        self.panel=3
    def opcion(self):
        if self.panel==1:
            print("Microondas en función calentar")
        elif self.panel==2:
            print("Microondas en función cocinar")
        else:
            print("Microondas en función dorar")

microondas1=microondas()
microondas1.dorar()
microondas1.opcion()

print("\nFin de los ejercicios 2\n")