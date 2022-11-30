
import smtplib
import Emisor as em
import Mensaje as ms


## Opción 1: Correos de Contactos en forma de listaA (Opción 1.1 de ListadeContactos.txt)

listaA=[]

message = 'Subject:{}\n\n{}'.format(ms.m1.subject,ms.m1.message)  ## -- Se estructura el asunto del correo y el mensaje

server = smtplib.SMTP('smtp.gmail.com',587)      ## -- Conecta al puerto de gmail

server.starttls()

server.login(em.e1.email_from, em.e1.password)      ## -- Conexión al correo del emisor a través email y password

server.sendmail(em.e1.email_from,listaA,message)       ## -- Correo del emisor, correo del receptor, mensaje

server.quit()

print(f"Correo enviado a: {listaA}")


## Opción 2: Utilizando bucles y correos de contactos en forma de listaB (Opción 2.1 de ListadeContactos.txt)

listaB=[]

for i in listaB:

    message = 'Subject:{}\n\n{}'.format(ms.m1.subject,ms.m1.message)

    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login(em.e1.email_from, em.e1.password)

    server.sendmail(em.e1.email_from,i,message)

    server.quit()

    print(f"Correo enviado a: {i}")
print("\nOperación Finalizada")
