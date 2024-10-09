print(" ")
print("Francisco Santiago Carrasco Correa 0421 3°W 08/10/24")
print(" ")
# funcion que muestra el saludo "hey amigos"
def saludoamigos():
    return "hey amigos"

# se usa el while para usar un bucle
while True:
    print(saludoamigos())
    respuesta = input("quieres volver a escuchar 'hey amigos'? (si/no): ").strip().lower()
    if respuesta != 'si':
        break