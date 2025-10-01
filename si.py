def afirma():
    
    while True:
        di = input("Escribe si para continuar: ").strip().lower()
        if di == "si":
            print("¡Perfecto! Continuamos.")
            break
    
    
afirma()