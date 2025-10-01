def escalera_inversa():
    
    while True:
        try:
            r = int(input("Ingresa un número mayor que 1: "))
            if r > 1:
                print("\nEscalera generada:\n")
                for i in range(r, 0, -1):    # escalera inversa
                    print("*" * i)
                break
            else:
                print("Incorrecto, el número debe ser mayor a 1")
                
        except ValueError:
            print("Error, ingrese un dato válido")
            
escalera_inversa()


#escalera inversa pero con la mejora de permitir al usuario generar más de una escalera sin tener que reiniciar el programa.

def escalera_inversa2():
    while True:
        try:
            r2 = int(input("Ingresa un número mayor que 1: "))
            if r2 > 1:
                print("\nEscalera generada:\n")
                for i in range(r2, 0, -1):
                    print("*" * i)
                print()  # salto de línea para estética
                
                # preguntar si quiere continuar
                opcion = input("¿Quieres generar otra escalera? (s/n): ").lower()
                if opcion != "s":
                    print("\nPrograma finalizado. ¡Hasta luego!\n")
                    break
            else:
                print("Incorrecto, el número debe ser mayor a 1\n")
        except ValueError:
            print("Error, ingrese un dato válido\n")

escalera_inversa2()
