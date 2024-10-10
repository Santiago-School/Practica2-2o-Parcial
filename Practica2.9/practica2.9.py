print("Francisco Santiago Carrasco Correa 0421 3°W 09/10/24")
print(" ")

def sum(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

def multip(numeros):
    total = 1
    for numero in numeros:
        total *= numero
    return total

# ejemplo de uso
lista = [1, 2, 3, 4]

resultadosuma = sum(lista)
resultadomultiplicacion = multip(lista)

#utilizando el print para mostrar los resultados
print("la suma de la lista es:", resultadosuma)
print("la multiplicacion de la lista es:", resultadomultiplicacion)
