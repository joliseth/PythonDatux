
## Creación de la Lista de Correos de los Receptores

## Opción 1: Adición de los correos a un archivo (ejm: "ListadeContactos.txt") y convertirlos a una lista.
  
print("\nDigite los emails que desea agregar al archivo txt, digite 'stop' para culminar el proceso\n")

email=input("Ingrese email: ")  

with open("PythonDatux/Proyecto/ListadeContactos.txt","w") as file: 
    while email !="*":
        file.write(email+",")   ## indica que registrará los emails en el archivo indicado
        email=input("Ingrese email: ")
        if email=="*":              
            break;
    print("Correos añadidos al archivo ListadeContactos.txt")

## -- 1.1 Ordenar correo de forma indivudual en una Lista

file=open("PythonDatux/Proyecto/ListadeContactos.txt")
text=file.read()
texto=text[:-1]     ## -- Elimina el ultimo caracter

listaA=texto.split(',')
print(listaA)


## Opción 2: Convertir un archivo (ejm: "ListadeContactos.txt") con correos en una lista.

file=open("PythonDatux/Proyecto/ListadeContactos.txt", "r")
listaB=[]

## -- 2.1 En este caso el archivo contiene un correo por fila

for line in file:
    line=line.strip()   ## Eliminar los espacios en blanco anteriores y posteriores de la linea que se lee
    listaB.append(line)
print(listaB)
