def positivo():
    
    while True:
        try:
            
            num = int(input("Ingresa un número mayor que cero: "))
            if num > 0:
                print(f"¡Correcto! El número ingresado es {num}")
                break
        except ValueError:
            print("Error, ingrese un valor válido")
        
        
positivo()