nombre = input("Ingrse su nombre: ") # Si forzamos (casteamos) un INT o un FLOAT nos va a dar error de tipo al querer concatenar (+) en la salida int() o float()
apellido = input("Ingrese su apellido: ")

print("Hola "+nombre+" "+apellido+" bienvenid@")

longitud = len(nombre)

#print("Tu nombre tiene",longitud,"caracteres")

# f-string
print(f"Tu nombre tiene {longitud} caracteres") 

# les dejo un truco para "modo debug"
print("truco modo debug\n")
print(f"Tu nombre tiene {longitud=} caracteres") #al escribir asi, muestra la variable con el valor

# operador modulo (old school o estilo C)
print("Tu nombre tiene %i caracteres") # el modulo (%) va acompañado de la inicial del tipo de dato a mostrar, en este caso una i de int


# format string
print("Tu nombre tiene {} caracteres".format(longitud))
print("Tu nombre tiene {l} caracteres".format(l=longitud))


#print("La ultima letra de tu nombre es:",nombre[-8]) # g[0]a[1]b[2]r[3]i[4]e[5]l[6]


'''
comentario en bloque
'''

texto = "hola mundó"
#texto2 = "hOLa MuNDo"

"""
print(texto.upper()) # el parentesis al final indica que vamos a ejecutar al llegar a esa linea
print(texto == texto2.lower())
print(texto2.lower())


print(texto)

"""