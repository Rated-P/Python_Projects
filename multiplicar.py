def multiplicar():
    
    while True:
        try:
            y = int(input("Ingresa un número mayor que cero: "))
            if y >= 1:
                print(f"\nTabla del {y}\n")
                for i in range(1, 11):
                    print(i, "x", y, "=", i*y,)
                        
                opcion = input("\nDesea volver a intentarlo? (si/no): ").lower().strip()
                if opcion != "si":
                    print("Gracias, esto ha sido todo")
                    break
                
            else:
                print("Incorrecto, el número debe ser mayor que 0\n")
                
        except ValueError:
                
            print("Error, introduzca un dato válido\n")
            
multiplicar()