
import ListadeEjercicios3 as LE3

print("\nLISTA DE EJERCICIOS 3\nAlumna: Joanna Lapa\n")

## PREGUNTA 1    

print("PREGUNTA 1\n")

p1=LE3.Pais("Perú","Lima","Español")
p2=LE3.Pais("Brasil","Brasilia","Portugues")

print(p1)
print(p1.nombre)
print(p1.capital)
print(p1.idioma)
print(p2)
p1.numHabitantes(33000000)
p2.numHabitantes(50000000)


## PREGUNTA 2

print("\nPREGUNTA 2\n")

p1=LE3.Producto("Celular","prod01",3500)
print(p1)

p2=LE3.Producto("Laptop","prod02",5000)
p3=LE3.Producto("Tablet","prod03",2500)

c1=LE3.Catalogo(p1)
c1.agregarProd(p2)
c1.agregarProd(p3)
c1.mostrarLista()


## PREGUNTA 3

print("\nPREGUNTA 3")

a1=LE3.Perro("kimba","perro")
a2=LE3.Gato("Haru","gato")

print(a1)
a1.datosContacto("Carlos Muñoz",968999555,"Los pinos 191")
a1.sonidoAnimal()

print(a2)
a1.datosContacto("Karen Diaz",968994444,"Las flores 305")
a2.sonidoAnimal()