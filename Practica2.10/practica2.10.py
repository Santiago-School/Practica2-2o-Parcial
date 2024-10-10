print("Francisco Santiago Carrasco Correa 0421 3°W 09/10/24")
print(" ")

def esvocal(caracter):
    # definimos las vocales
    vocales = "aeiouAEIOU"
    # verificamos si el carácter está en la lista de vocales
    return caracter in vocales

# ejemplo de uso
caracter = input("ingresa un caracter: ")

if esvocal(caracter):
    print(caracter, "es una vocal")
else:
    print(caracter, "no es una vocal")
