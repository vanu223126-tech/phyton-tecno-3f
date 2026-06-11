
#Cree una funcion que calcule el promedio de N notas

def calcular_promedio(notas, decimales=2):
    if not notas:
        return None
    return round(sum(notas) / len(notas), decimales)


print(calcular_promedio([8, 9, 7]) )      # usa 2 decimales por defecto
print(calcular_promedio([8, 9, 7], 0)   )  # sin decimales
print(calcular_promedio([8, 9, 7], 4))    # con 4 decimales



#Cree una funcion que determine si un color es primario o no, se debe imprimir por pantalla la leyenda “el color X es primero “ o “el color X no es primario”#

def es_color_primario(color):
    colores_primarios = ["rojo", "azul", "amarillo"]
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario.")  
    else:
        print(f"El color {color} no es primario.")   


    print (es_color_primario("rojo"))
    print (es_color_primario("verde"))
    print (es_color_primario("Azul"))    



#Cree una funcion que determine que numero de una serie de N numeros es mayor

def encontrar_mayor(numeros):
    if not numeros:
        return None
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor
    
print(encontrar_mayor([3, 7, 2, 9, 5]))  # devuelve 9


#Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el usuario#

def dibujar_rectangulo(filas, columnas):
    for i in range(filas):
        print("* " * columnas)

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))



#Cree una funcion que calcule el Factorial de un numero entero positivo

def calcular_factorial(numero):
    if numero < 0:
        print("El número debe ser positivo.")
        return None
    
    if numero == 0 or numero == 1:
        return 1
    
    factorial = 1
    for i in range(2, numero + 1):
        factorial = factorial * i
    
    print(f"El factorial de {numero} es: {factorial}")
    return factorial


# Pedimos el número al usuario
numero = int(input("Ingresá un número entero positivo: "))
calcular_factorial(numero)