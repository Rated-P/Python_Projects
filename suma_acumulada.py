def sumando():
    while True:
        try:
            n = int(input("Introduce un número entero positivo: \n"))
            if n > 0:
                suma = 0   # Acumulador
                for i in range(1, n + 1):
                    suma += i
                    print(f"La suma acumulada es igual a {suma}")
                    
                continuar = input("\nDesea volver a intentarlo? [si/no]: \n").lower().strip()
                if continuar == "no":
                    print("Gracias, eso ha sido todo\n")
                    break
                
            else:
                print("\nIncorrecto, introduzca un número mayor que cero\n")
                
        except ValueError:
            print("Introduzca un dato válido\n")
            
sumando()
