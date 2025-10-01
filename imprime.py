def imprimir():
    while True:
        try:
            num = int(input("Ingresa un número por encima de 1: "))
            if num >= 1:
                for Python in range(num):
                    print("Python")
                break
            else:
                print("Incorrecto")
                
        except ValueError:
            print("Incorrecto, ingrese un dato válido")
            
imprimir()

"""
versión mejorada
"""

def imprime():
    while True:
        try:
            num = int(input("Ingresa un número entero mayor o igual que 1: "))
            if num >= 1:
                for i in range(num):
                    print("Python")
                break
            else:
                print("Error: el número debe ser mayor o igual que 1.")
        except ValueError:
            print("Error: ingresa un número entero válido.")

imprime()

"""
🔧 Aspectos a mejorar

Nombre de la variable en el for: pusiste for Python in range(num):.

Aunque funciona, no es buena práctica usar el nombre de un lenguaje o palabra con mayúscula como variable. Mejor usa algo como for i in range(num):.

Claridad en mensajes de error:

En lugar de "Incorrecto", sería más claro algo como:

"Error: ingresa un número entero mayor o igual que 1."

"Error: ingresa un valor numérico válido."

Condición de entrada:

El enunciado pedía positivo (>= 1). Tú lo cumpliste, pero tu mensaje dice "por encima de 1", lo que confunde porque en realidad aceptas 1.

Legibilidad menor:

Espacios y nombres más claros (num está bien, pero podrías haber usado cantidad o veces)
"""