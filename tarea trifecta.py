

control = True

while control:
    print("\n--- Inicio del ciclo ---")


    entrada= input("Ingrese un número entero: ")

    if entrada.isdigit():
        numero = int(entrada)
        
        if numero == 0:
            print("Se ingreso el numero 0.Programa finalizado")

            control = False

        else:
            print("¡Numero Valido! Iniciando...")

            frase=input("Ingrese una palabra o frase:")
            cantidad_caracteres = len(frase)
            print(f"La palabro o frace tiene {cantidad_caracteres} caracteres.")

            factorial = 1
            for i in range(1, cantidad_caracteres + 1):
                factorial = factorial * i

            print(f"El factorial de {cantidad_caracteres} es: {factorial}")

            if factorial % 2 == 0:
                print("El resultado del factorial es PAR.") 
            else:
                print("El factorial es IMPAR.")      

            print("Reiniciando verificacion....")

    else:
        print("Entrada inválida (no es un número entero). Programa finalizado.")
        control = False        

