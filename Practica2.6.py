print(" ")
print("Francisco Santiago Carrasco Correa 0421 3°W 09/10/24")
print(" ")

#se define la variable para conseguir atraves del texto
email = input("ingresa tu direccion de email: ")

def emailvalido(email):
    return "@" in email

#si se tiene la @ se pone valido, de lo contrario no lo hara
if emailvalido(email):
    print("la direccion de email es valida")
else:
    print("la direccion de email no es valida")
