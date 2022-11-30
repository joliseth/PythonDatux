
class Mensaje:

    def __init__(self, subject, message):
        self.subject=subject
        self.message=message
    def __str__(self):
        return "El asunto y mensaje fueron registrados"

asunto_correo=str(input("Ingrese asunto: "))
mensaje_correo=str(input("Ingrese mensaje: "))

m1=Mensaje(asunto_correo,mensaje_correo)

if __name__== '__main__':
    print(m1)
    print(m1.subject)
    print(m1.message)
