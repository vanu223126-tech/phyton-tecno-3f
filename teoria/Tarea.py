
"""Este programa le pide al usuario su nombre
y lo muestra en mayuscula"""

nombre = input("Ingrese su nombre: ")
print (nombre.upper())

""" Este progra le pide al usuario que ingrese un numero 
le sume 5 y lo muestre en pantalla"""

numero = int(input("Ingresa un numero:"))
resultado= numero + 5
print ("El resultado es",resultado)

"""Este programa pide el nombre y apellido
y luego muestra un saludo en pantalla."""

nombre= input("Ingrese su nombre:")
apellido= input("Ingrese su apellido")
print("Hola " + nombre + " " + apellido + " Bienvenido")

""" Este programa le pide al usuario
que ingrese 5 numero y realize el promedio y muestre el resultado en pantalla"""

numero1=int(input("Ingrese el primer numero:"))
numero2=int(input("Ingrese el segundo numero:"))
numero3=int(input("Ingrese el tercer numero:")) 
numero4=int(input("Ingrese el cuarto numero:"))
numero5=int(input("Ingrese el quinto numero:"))
Promedio= numero1 + numero2+numero3+numero4+numero5/5
print("El resultado es",Promedio)


""" Este programa le pide al usuario cualquier frase y la ingresa en minuscula"""

frase=input("Ingrese una Frase:")
resultado= frase.lower()
print("La frase en minuscula es:", resultado)

