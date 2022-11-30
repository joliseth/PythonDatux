
if __name__== '__main__':

    print("\nLISTA DE EJERCICIOS 3\nAlumna: Joanna Lapa\n")

## PREGUNTA 1
## Definir la siguiente clases con sus métodos iniciales y su método __str__

    print("PREGUNTA 1\n")

class Pais:
    habitantes=0
    def __init__(self,nombre,capital,idioma):
        self.nombre=nombre
        self.capital=capital
        self.idioma=idioma
    def __str__(self):
        return f'El pais es {self.nombre}, su capital es {self.capital} y su idioma oficial es {self.idioma}'
    def numHabitantes(self,habitantes:int):
        print(f'{self.nombre} tiene {habitantes} habitantes')

   
## PREGUNTA 2
## Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
## clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
## tener un método para agregar productos y otra para mostrar toda la lista de productos.

if __name__== '__main__':

    print("\nPREGUNTA 2\n")

class Producto:
    def __init__(self, nombre, codigo, precio):
        self.nombre=nombre
        self.codigo=codigo
        self.precio=precio
        print(f'Se ha registrado en el sistema el producto: {self.nombre} ')
    def __str__(self):
        return f'- {self.nombre} se ha registrado con el código {self.codigo} y precio {self.precio}'

class Catalogo:
    listaProducto=[]
    def __init__(self, producto):
        self.listaProducto.append(producto)

    def agregarProd(self, producto):
        self.listaProducto.append(producto)
        
    def mostrarLista(self):
        print("\nLa lista de producto es: ")
        for producto in self.listaProducto:
            print(self.listaProducto.index(producto)+1,producto)            

 
## PREGUNTA 3
## Crear una clase Animal ,luego una clase Perro y gato que sean hijos de Animal ,el método
## de Sonido debe ser diferente

if __name__== '__main__':
    
    print("\nPREGUNTA 3")

class Animal:
    def __init__(self, nombre, tipo):
        self.nombre=nombre
        self.tipo=tipo
    def __str__(self):
        return f'\nEl animal es {self.tipo} y su nombre es {self.nombre}'
    def datosContacto(self, dueño, celular, direccion):
        self.dueño=dueño
        self.celular=celular
        self.direccion=direccion
        print(f'- Nombre del dueño es {dueño} / Celular: {celular} / Dirección: {direccion}')
        
class Perro(Animal):
    def sonidoAnimal(self):
        print(f"- El sonido que hace el animal es Guau")
        
class Gato(Animal):
    def sonidoAnimal(self):
        print(f"- El sonido que hace el animal es Miau")

if __name__== '__main__':

## PREGUNTA 4
## Con la librería os (import os ) usar 3 funciones de la libreria e imprimir su resultado
## referencia: https://docs.python.org/3/library/os.html

    print("\nPREGUNTA 4\n")

    import os

        ## Mostrar ruta actual de trabajo
    print(os.getcwd())

        ## Visualizar carpetas y archivos que hay en la ruta actual o carpeta específica
    print(os.listdir())
    print(os.listdir('Clase 2'))

        ## Crear una nueva carpeta
    os.mkdir("nueva carpeta")

        ## Añadir una carpeta creada a la ruta actual
    os.chdir("nueva carpeta")

        ## Unir paths/rutas
    print(os.path.join(os.getcwd(),"Clase 2"))


    ## PREGUNTA 5
    ## Imprimir el nombre del archivo ejecutado

    print("\nPREGUNTA 5\n")

    import sys
    import os

    variable =sys.argv[0]

    print(f'La ruta de trabajo es: {variable}')

    name_file=os.path.basename(variable)

    print(f'El nombre del archivo es: {name_file}')    


    ## PREGUNTA 6
    ## Genera un número aleatorio entre 1 y 100

    print("\nPREGUNTA 6\n")

    import random

    a = random.randrange(1,100)
    print(f'Número aleatorio entero: {a}')

    b = round(random.uniform(1,100),2)
    print(f'Número aleatorio decimal: {b}')

    ## 7 números aleatorios para la lotería

    loteria=[]
    j=random.randrange(1,100)

    while len(loteria)<7:
        loteria.append(j)
        j=random.randrange(1,100)
    print(f'El número de la lotería es: {loteria}')


    ## PREGUNTA 7
    ## Hacer un programa que consulte el valor del dolar (compra y venta ) de la fecha actual
    ## segun sunat (url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat')

    print("\nPREGUNTA 7\n")

    import requests

    link = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'

    conect = requests.get(link)

    answer = conect.json()

    compraDolar = answer["compra"]
    ventaDolar = answer["venta"]

    print(answer)
    print(compraDolar, ventaDolar,"\n")

    opcion=int(input("Digite opción 1 para Compra o 2 para Venta\nIngrese opción: "))
    monto=float(input("Ingrese cantidad a cambiar: "))

    if opcion == 1:
        print(f'La compra del dolar es {compraDolar}, Ud. recibirá {monto*compraDolar}')
    elif opcion == 2:
        print(f'La venta del dolar es {ventaDolar}, Ud. recibirá {monto*ventaDolar}')
    else:
        print("Opción no es valida")


    ## PREGUNTA 8
    ## Buscar si existe la palabra python en el siguiente texto “Python es uno de los lenguajes de
    ## programación dinámicos más populares que existen entre los que se encuentran Java,
    ## Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje "scripting", es
    ## realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo,
    ## desde simples "scripts", hasta grandes servidores web que proveen servicio ininterrumpido
    ## 24×7. Es utilizado para la programación de interfaces gráficas y bases de datos,
    ## programación web tanto en el cliente como en el servidor (véase Django o Flask) y "testing"
    ## de aplicaciones”.

    print("\nPREGUNTA 8\n")

    import re

    miTexto = "Python es uno de los lenguajes de programación dinámicos más populares que existen entre los que se encuentran Java, Javascript, Go y 'C#'. Aunque es considerado a menudo como un lenguaje scripting, es realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo, desde simples scripts, hasta grandes servidores web que proveen servicio ininterrumpido 24x7. Es utilizado para la programación de interfaces gráficas y bases de datos, programación web tanto en el cliente como en el servidor (véase Django o Flask) y testing de aplicaciones"
    palabra = "Python"

    encontrarPalabra = re.search(palabra,miTexto)

    if encontrarPalabra:
        print(f"Encontró la palabra {palabra}\n")
    else:
        print(f"No encontró la palabra {palabra}\n")


    ## PREGUNTA 9
    ## Obtener todas las ocurrencias de la palabra python en el texto anterior.

    print("PREGUNTA 9\n")

    for r in re.findall(palabra, miTexto):
        print('Palabra encontrada: %s' %r)


    print("\nFin de los ejercicios 3\n")