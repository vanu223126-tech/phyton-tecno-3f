import os

"""
while True:
    numero = input("Ingrese su nombre: ")
    if numero.isalpha():
        break
    else:
        os.system("cls")
        print("Ingresa su nombre solo con letras \n")
    


print(f"El nombre ingresado es : {numero}")
#print(type(numero))
"""

suma = 0

for i in range(5):
    while True:
        numero = input(f"Ingrese nota {i+1}° : ")
        if numero.isdigit():
            suma += int(numero) # suma = suma + numero
            break
        else:
            os.system("cls")
            print("Ingresa un numero entero positivo \n")

print(i)
print(f"Su promedio es: {suma/(i+1)}")