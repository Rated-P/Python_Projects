def escalera():
    
    while True:
        try:
            rango = int(input("Ingresa un número mayor que 1: "))
            if rango > 1:
                for i in range(1, rango + 1):
                    print("*" * i)
                break
            else:
                print("Incorrecto, el número debe ser mayor a 1")
        except ValueError:
            print("Error, ingrese un dato válido")
            
escalera()