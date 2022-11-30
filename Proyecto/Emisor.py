
class Emisor:

    def __init__(self, email_from, password):
        self.email_from=email_from
        self.password=password
        
    def __str__(self):
        return "Los datos de autentificación son privados"

correo_emisor=str(input("Ingrese correo de emisor: "))
contraseña_emisor=str(input("Ingrese contraseña de correo: "))

e1=Emisor(correo_emisor,contraseña_emisor)

if __name__== '__main__':
    print(e1)
    print(e1.email_from)
    print(e1.password)
    






